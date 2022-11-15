import csv
import json
import requests
import os
import time

#creating global variables for the csv file so it is useable on any machine and for the url
CSV_FILE = os.getcwd() + "/users.csv"
USER_URL = "https://random-data-api.com/api/v2/users"

def get_data():
    """
    this function receives the data from the api in json format and converts it into a dictionary format
    """
    data = {}
    response = requests.get(USER_URL)
    #it checks if the api is available
    if response.status_code == 200:
        json_data = json.loads(response.text)
        data = {
            'ID': json_data['id'],
            'First Name': json_data['first_name'],
            'Last Name': json_data['last_name'],
            'Username': json_data['username'],
            'email': json_data['email'],
            'date_of_birth': json_data['date_of_birth'],
            'gender': json_data['gender'],
            'phone_number': json_data['phone_number']
        }
    else:
        print("Error getting data, retrying")
    return data


def write_data_into_csv(data):
    """
    takes the data(dictionary) and appends it to the csv file
    """
    #checks if the data is avialable
    if data:
        #checks if it is the first entry of the csv 
        first_entry = False if os.path.exists(CSV_FILE) else True

        #opens the csv file to write the data into csv
        with open(CSV_FILE, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            #if its the first entry the headers are appended to the csv
            if first_entry:
                header = data.keys()
                csv_writer.writerow(header)
            #the data is added to the csv 
            csv_writer.writerow(data.values())
    return


def run():
    while True:
        #sleeps the program for one second before pulling the data from the api and adding it to the csv
        time.sleep(1)
        #
        write_data_into_csv(data=get_data())

run()
