#!/usr/bin/python3
"""a python script to gather data from an api """
import requests
import os
import sys

user_id = int(sys.argv[1])
completed_tasks = 0
total_tasks = 0

response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
user_data = response.json()

name = user_data['name']

todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id))

todo_list = todos.json()

for task in todo_list:
    if task['completed'] == True:
        completed_tasks = completed_tasks + 1
    total_tasks = total_tasks + 1

print("Employee {} is done with tasks({}/{})".format(name, completed_tasks, total_tasks))
for task in todo_list:
    if task['completed'] == True:
        print("\t {}".format(task['title']))
