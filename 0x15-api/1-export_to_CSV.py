#!/usr/bin/python3
"""
Python script that exports user's TODO list progress in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    with open('{}_todo.csv'.format(employee_id), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['userId', 'task', 'completed', 'title'])
        for todo in todos:
            csvwriter.writerow([employee_id, todo.get("id"), todo.get("completed"), todo.get("title")])
