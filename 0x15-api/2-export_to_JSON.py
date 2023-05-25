#!/usr/bin/python3
"""
    Using Python Requests module to gather some
    info but now store it in csv format
"""
import json
import requests
import sys

if __name__ == "__main__":
    userid = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users/{}".format(userid)
    res = "https://jsonplaceholder.typicode.com/users/{}/todos".format(userid)

    username = requests.get(users).json()['username']
    todo_data = requests.get(res).json()

    filename = "{}.json".format(userid)

    list = []
    for todo in todo_data:
        completed = todo['completed']
        task = todo['title']
        data = {"task": task, "completed": completed, "username": username}
        list.append(data)
    all_data = {userid: list}
    json_data = json.dumps(all_data)

    with open(filename, "w") as file:
        file.write(json_data)
