#!/usr/bin/python3
"""
    Using Python Requests module to gather some
    info but now store it in csv format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users/{}".format(user)
    res = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user)

    username = requests.get(users).json()['username']
    todo_data = requests.get(res).json()

    filename = "{}.csv".format(user)

    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            row = [user, username, todo.get('completed'), todo.get('title')]
            row = [str(value) for value in row]
            csv_writer.writerow(row)
