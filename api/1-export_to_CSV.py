#!/usr/bin/python3

"""Export to CSV"""
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
        if item.get('completed'):
            completed_tasks += 1
    user_id = str(employee_id)
    user_name = users_response.get('username')

    for todo in todos_response:
        todo_title = todo.get('title')
        todo_status = todo.get('completed')
        with open(str(user_id) + '.csv,' 'w') as file:
            [file.write('"' + user_id + '",' +
                        '"' + user_name + '",'
                        '"' + str(todo_status) + '",' +
                        '"' + todo_title + '",' + "\n")
             for todo in todos_response]
