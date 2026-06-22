tasks = [
    {"title": "Learn Python function", "done": True},
    {"title": "Practice GitHub push", "done": False},
]


def show_tasks() -> None:
    for index, task in enumerate(tasks, start=1):
        status = "done" if task["done"] else "todo"
        print(f"{index}. [{status}] {task['title']}")


if __name__ == "__main__":
    show_tasks()
