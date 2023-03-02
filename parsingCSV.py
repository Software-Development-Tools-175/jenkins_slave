import csv

def extractCSV():
  rows = []

  with open("args.csv") as file:
      csvreader = csv.reader(file)
      header = next(csvreader)
      for row in csvreader:
          rows.append(row)

      for item in rows:
        print("Member No. " + item[0] + " " + item[1] + " " + item[2] + " is " + item[3] + " years old")

extractCSV()

