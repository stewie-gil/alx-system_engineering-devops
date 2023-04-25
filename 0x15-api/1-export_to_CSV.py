#!/usr/bin/python3
"""
Python script to print out todo list info
"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    usr_url = "https://jsonplaceholder.typicode.com/users/{}"
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    user1 = usr_url.format(employee_id)
    todo1 = todo_url.format(employee_id)

    u = requests.get(user1).json()
    todo_list = requests.get(todo1).json()
    with open('{}.csv'.format(id), 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for t in todo_list:
            row = [id, u.get("username"), t.get("completed"), t.get("title")]
            row = [str(value) for value in row]
            csv_writer.writerow(row)
