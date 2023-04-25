#!/usr/bin/python3
"""
Python script to print out todo list info
"""
import json
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
    with open('{}.json'.format(employee_id), 'w') as json_file:
        tasks = []
        for t in todo_list:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": u.get("username")})
        data = {"{}".format(employee_id): tasks}
        json.dump(data, json_file)
