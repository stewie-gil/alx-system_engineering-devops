#!/usr/bin/python3
"""
Script that retrieves information about a specified employee's Todo
"""

import requests
import sys

# Define the base URL for the JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    # Get the employee ID from the command line arguments
    emp_id = sys.argv[1]

    # Construct the URLs for the employee and Todo list endpoints
    emp_url = f"{BASE_URL}/users/{emp_id}"
    todo_url = f"{BASE_URL}/users/{emp_id}/todos"

    # Retrieve the employee and Todo list data from the API
    employee = requests.get(emp_url).json()
    todo_items = requests.get(todo_url).json()

    # Calculate the number of completed tasks and collect their titles
    num_completed_tasks = 0
    completed_tasks = []
    total_num_tasks = len(todo_items)

    for item in todo_items:
        if item.get("completed"):
            num_completed_tasks += 1
            completed_tasks.append(item.get("title"))

    # Construct the output sentence and print it to the console
    if num_completed_tasks == 1:
        task_str = "task"
    else:
        task_str = "tasks"

    sentence = f"Employee {employee.get('name')} is done \
with {num_completed_tasks} {task_str} out of {total_num_tasks}:"
    print(sentence)

    for task in completed_tasks:
        print(f"\t{task}")
