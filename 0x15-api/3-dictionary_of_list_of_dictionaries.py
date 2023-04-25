#!/usr/bin/python3
"""
Python script to export user's task list in JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    d = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(d)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(d)

    user = requests.get(user_url).json()
    todo_list = requests.get(todo_url).json()

    with open('{}.json'.format(employee_id), 'w') as json_file:
        tasks = []
        for task in todo_list:
            tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            })
        data = {"{}".format(employee_id): tasks}
        json.dump(data, json_file)
