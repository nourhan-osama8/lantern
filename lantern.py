
import argparse

parser = argparse.ArgumentParser(description="Lantern Task Tracker")
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
list_parser = sub.add_parser("list")

list_parser.add_argument(
    "--done",
    action="store_true",
)

args = parser.parse_args()

# Temporary sample data
tasks = [
    {"title": "Study Python", "done": True},
    {"title": "Practice Git", "done": False},
    {"title": "Read documentation", "done": True}
]

if args.command == "add":
    print("Add command")

elif args.command == "list":

    if args.done:
        tasks = [task for task in tasks if task["done"]]

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task["title"])
