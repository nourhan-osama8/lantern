import argparse
from tasks import list_tasks

parser = argparse.ArgumentParser(description="Lantern Task Tracker")
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
list_parser = sub.add_parser("list")


list_parser.add_argument("--done", action="store_true")

list_parser.add_argument(
    "--sort",
    action="store_true",
    help="Sort tasks alphabetically by title"
)

args = parser.parse_args()

if args.command == "add":
    print("Add command")

elif args.command == "list":
    tasks = list_tasks()

    if args.done:
        tasks = [task for task in tasks if task.get("done")]

    if not tasks:
        print("No tasks found.")
    else:
        print("List command")