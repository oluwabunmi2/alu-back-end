#!/usr/bin/python3

"""Export to CSV"""
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos" \
        .format(employee_id)
    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    total_tasks = 0
    completed_tasks = 0

    for item in todos_response:
        if item.get("completed"):
            completed_tasks += 1

    user_id = str(employee_id)
    user_name = user_response.get("username")
    employee_name = user_response.get("name")

    for todo in todos_response:
        todo_title = todo.get("title")
        todo_status = todo.get("completed")

        with open(str(employee_id) + '.csv', "w") as file:
            [file.write('"' + str(employee_id) + '",' +
                        '"' + user_name + '",' +
                        '"' + str(task["completed"]) + '",' +
                        '"' + task["title"] + '",' + "\n")
             for task in todos_response]
