import csv
import spacy

assets = ['train', 'test']
file =  open ('Train.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
for row in csvreader:
        rows.append(row)
text = ""

for row in rows:
    text += row[1]
text = text.replace("\n", " ")
text = text.split(".")

longest = 0
print ( len(text) )

for line in text:
    if ( len(line) > longest ):
        longest = len(line)

print(longest)