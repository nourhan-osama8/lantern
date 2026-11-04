import argparse
from tasks import list_tasks
from export import export_csv

parser = argparse.ArgumentParser(description="Lantern Task Tracker")
sub = parser.add_subparsers(dest="command")
add_parser = sub.add_parser("add")
list_parser = sub.add_parser("list")
list_parser.add_argument("--done", action="store_true")
export_parser = sub.add_parser("export")
export_parser.add_argument("--csv", action="store_true")
args = parser.parse_args()

if args.command == "add":
    print("Add command")
elif args.command == "export":
    if args.csv:
        export_csv(list_tasks())

elif args.command == "list":
    tasks = list_tasks()

    if args.done:
        tasks = [task for task in tasks if task.get("done")]

    if not tasks:
        print("No tasks found.")
    else:
        print("List command")