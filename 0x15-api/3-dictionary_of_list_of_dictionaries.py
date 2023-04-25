#!/usr/bin/python3
"""
    Python script that exports data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    usr_url = "https://jsonplaceholder.typicode.com/users"
    tds_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(usr_url).json()
    todo_list = requests.get(tds_url).json()

    with open('todo_all_employees.json', 'w') as json_file:
        data = {}
        for user in users:
            user_id = user.get("id")
            user_name = user.get("username")
            tasks = []
            for task in todo_list:
                if task.get("userId") == user_id:
                    tasks.append({"task": task.get("title"),
                                  "completed": task.get("completed"),
                                  "username": user_name})
            data["{}".format(user_id)] = tasks

        json.dump(data, json_file)
