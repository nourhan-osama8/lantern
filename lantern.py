import argparse


parser = argparse.ArgumentParser(description="Lantern Task Tracker")
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
list_parser = sub.add_parser("list")
list_parser.add_argument("--done", action="store_true")


args = parser.parse_args()

if args.command == "add":
    print("Add command")

elif args.command == "list":
    print("List command")