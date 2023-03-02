import csv

def extractCSV():
  rows = []

  with open("args.csv") as file:
      csvreader = csv.reader(file)
      header = next(csvreader)
      for row in csvreader:
          rows.append(row)

      for item in rows:
        println("${item[1]} ${item[2]} with age ${item[3]} has id ${item[0]}")

extractCSV()

