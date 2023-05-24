#!/usr/bin/python3
"""
    Using Python Requests module to gather some
    information about a user
"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users/{}".format(user)
    res = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user)

    name = requests.get(users).json()['name']
    todo_data = requests.get(res).json()

    completed = 0
    not_completed = 0

    for todo in todo_data:
        if todo['completed'] is True:
            completed = completed + 1
        else:
            not_completed = not_completed + 1
    print("Employee {} is done with tasks({}/{}):".format
          (name, completed, completed + not_completed))

    for todo in todo_data:
        if todo['completed'] is True:
            print("\t {}".format(todo['title']))
