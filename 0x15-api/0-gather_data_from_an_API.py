#!/usr/bin/python3
"""
Python script to print out todo list info
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    usr_url = "https://jsonplaceholder.typicode.com/users/{}"
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    user1 = user_url.format(employee_id)
    todo1 = todo_url.format(employee_id)

    user = requests.get(user1).json()
    todo_list = requests.get(todo1).json()
    completed = 0
    total = 0
    completed_list = []

    for task in todo_list:
        total += 1
        if task.get("completed") is True:
            completed += 1
            completed_list.append(task.get("title"))

    printing = "Employee {} is done with tasks({}/{}):"

    print(printing.format(user.get("name"), completed, total))
    for task in completed_list:
        print("\t {}".format(task))
