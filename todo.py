import argparse

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    try:
        task = tasks.pop(index - 1)
        print(f"Deleted task: {task}")
    except IndexError:
        print("Invalid task index.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI Tool")
    parser.add_argument('--add', type=str, help="Add a new task")
    parser.add_argument('--list', action='store_true', help="List all tasks")
    parser.add_argument('--delete', type=int, help="Delete a task by its index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()
