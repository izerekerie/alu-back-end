#!/usr/bin/python3
import requests
import sys

def get_employee_name(employee_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    if response.status_code == 200:
        return response.json().get('name')
    else:
        print(f"Error: Unable to fetch employee details (Status code: {response.status_code})")
        sys.exit(1)

def get_todo_list(employee_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch TODO list (Status code: {response.status_code})")
        sys.exit(1)

def main(employee_id):
    employee_name = get_employee_name(employee_id)
    todo_list = get_todo_list(employee_id)

    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Error: The employee ID must be an integer")
        sys.exit(1)
