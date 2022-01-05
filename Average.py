import csv

with open('Scores.csv') as s:
    reader = csv.reader(s)
    for row in s:
        print (row.strip())
        name = row[0]
        # name = list(row)
        print (name)