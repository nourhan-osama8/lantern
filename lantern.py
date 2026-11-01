import argparse


parser = argparse.ArgumentParser(description="Lantern Task Tracker")
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
list_parser = sub.add_parser("list")


args = parser.parse_args()

if args.command == "add":
    print("Add command")

elif args.command == "list":
    print("List command")