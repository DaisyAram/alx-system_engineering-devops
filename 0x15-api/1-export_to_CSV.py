#!/usr/bin/python3
"""Returns to-do list information for a given employee ID
and exports data to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed_todos = [todo for todo in todos if todo["completed"]]
    total_todos = len(todos)

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in completed_todos:
            writer.writerow(
                {
                    "USER_ID": user_id,
                    "USERNAME": user["name"],
                    "TASK_COMPLETED_STATUS": "completed" if todo[
                        "completed"] else "not completed",
                    "TASK_TITLE": todo["title"],
                }
            )

            print("Employee {} is done with tasks({}/{}):".format(
                user["name"], len(completed_todos), total_todos))
            [print("\t {}".format(c["title"])) for c in completed_todos]
