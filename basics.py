import csv
import spacy
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
nlp = spacy.load("en_core_web_sm")
text_length = len(text)
nlp.max_length =  text_length
print(text_length)
doc = nlp(text)
print("done")