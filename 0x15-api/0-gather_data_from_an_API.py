#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json() if user_response.status_code == 200 else None

    if user is None:
        print("Error: Employee not found")
        sys.exit(1)

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json() if todos_response.status_code == 200 else []

    completed = [todo["title"] for todo in todos if todo["completed"]]
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed), len(todos)))
    for task in completed:
        print("\t" + task)
