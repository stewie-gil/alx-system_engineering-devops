#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    employee = requests.get(emp_url).json()
    todo_items = requests.get(todo_url).json()
    
    num_completed_tasks = 0
    completed_tasks = []
    total_num_tasks = 0
    completed_tasks = []

    for item in todo_items:
        total_num_tasks += 1
        if item.get("completed"):
            num_completed_tasks += 1
            completed_tasks.append(item.get("title"))

    if num_completed_tasks == 1:
        task_str = "task"
    else:
        task_str = "tasks"

    sentence = f"Employee {employee.get('name')} is done with {num_completed_tasks} {task_str} out of {total_num_tasks}:"
    print(sentence)
    
    for task in completed_tasks:
        print("\t" + task)
