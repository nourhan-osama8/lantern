import csv
import sys


def export_csv(tasks):
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(["title", "done"])

    for task in tasks:
        writer.writerow([task.get("title"), task.get("done")])