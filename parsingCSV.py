import csv

def extractCSV():
  rows = []

  with open("args.csv") as file:
      csvreader = csv.reader(file)
      header = next(csvreader)
      for row in csvreader:
          rows.append(row)

  print(rows)

extractCSV()

