#!/usr/bin/python3
"""Return information about an employess's TODO list progress using REST API."""

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requets.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    done = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
