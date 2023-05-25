#!/usr/bin/python3
"""
    Using Python Requests module to gather some
    info but now store it in csv format
"""
import json
import requests

if __name__ == "__main__":
    all_user_data = {}
    for i in range(1, 10):
        userid = i
        users = f"https://jsonplaceholder.typicode.com/users/{userid}"
        res = f"https://jsonplaceholder.typicode.com/users/{userid}/todos"
        username = requests.get(users).json()["username"]
        todo_data = requests.get(res).json()

        user_data = []
        for todo in todo_data:
            completed = todo["completed"]
            task = todo["title"]
            data = {"username": username, "task": task, "completed": completed}
            user_data.append(data)

        all_user_data[userid] = user_data

    filepath = "todo_all_employees.json"

    with open(filepath, "w") as file:
        json.dump(all_user_data, file)
