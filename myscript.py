import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="?", help="the CSV file")
args = parser.parse_args()


def printMember():
  rows = []
  greeting = ""

  with open(args.file) as file:
      csvreader = csv.reader(file)
      header = next(csvreader)
      for row in csvreader:
          rows.append(row)

  for item in rows:
    greeting += "Member No." + item[0] + item[1]+ item[2] + "is" + item[3] + " years old. \n"
    print(greeting)

printMember()
