import csv 
import os

#creating global variable for the csv file so it is useable on any machine and for the url
CSV_FILE = os.getcwd() + "/users.csv"

def read_csv():
    """
    reads the users.csv file and returns the a list of users 
    """
    data = csv.reader(open(CSV_FILE))
    next(data)
    user_list = []
    for rows in data :
        user_list.append(rows)
    return user_list

def search_users(data = read_csv()):
    """
    searches the list returned by the read_csv() function for and prints the relevant information of that user
    """
    uid = input("Enter the user ID to search: \n")
    flag = False
    for user in range(len(data)):
        if (data[user][0]) == uid:
            print(data[user])
            flag = True
            break
    if flag:
        pass
    else:
        print("Enter a valid user ID")

search_users()