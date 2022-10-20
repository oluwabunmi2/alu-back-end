#!/usr/bin/python3
"""module is to be documented"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    users_details = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_details = "https://jsonplaceholder.typicode.com/users/{}/todos" \
        .format(employee_id)

    users_response = requests.get(users_details).json()
    todos_response = requests.get(todos_details).json()

    total_tasks = 0
    completed_tasks = 0

    for item in todos_response:
        if item.get('userId') == int(employee_id):
            total_tasks += 1
        if item.get('completed'):
            completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(users_response.get('name'),
                  completed_tasks, total_tasks))
    for todo in todos_response:
        if todo.get('completed'):
            print("\t {}".format(todo.get("title")))
