import csv 
import os
import operator

#creating global variables for the csv files so it is useable on any machine 
CSV_FILE = os.getcwd() + "/users.csv"
SORTED_CSV_FILE = os.getcwd() + "/users-sorted.csv"


def delete_existing_csv():
    """
    deletes the csv if a csv file named users-sorted.csv already exists 
    """
    if os.path.exists(SORTED_CSV_FILE):
        os.remove(SORTED_CSV_FILE)

def read_csv():
    """
    reads the users.csv file and sorts the data as a list and returns that list
    """
    data = csv.reader(open(CSV_FILE))
    next(data)
    sorted_user_data = sorted(data, key=operator.itemgetter(1,3))
    return sorted_user_data

def write_sorted_user_csv(data = read_csv()):
    """Writes the sorted list to the new file called users-sorted.csv"""
    with open(SORTED_CSV_FILE, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        #writes the header
        header = ["ID","First Name","Last Name","Username","email","date_of_birth","gender","phone_number"]
        csv_writer.writerow(header)
        #loops the list and writes each row into the csv
        for i in range(len(data)):
            csv_writer.writerow(data[i])

delete_existing_csv()
write_sorted_user_csv()