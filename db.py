from eloquent import DatabaseManager, Model
import csv
import spacy


config = {
    "mysql": {
        "driver": "mysql",
        "host": "localhost",
        "database": "ml",
        "user": "admin",
        "password": "password",
        "prefix": "",
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

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
texts = text.split(".")


class Sentence(Model):
    __fillable__ = ["sentence", "source", "progress"]
    __table__ = "Sentence"
    __timestamps__ = False
    pass

class Token(Model):
    __fillable__ = ["token", "index", "sentenceId"]
    __table__ = "Token"
    __timestamps__ = False
    pass

for line in texts:
    index = 0
    line = line.strip()
    sentence = Sentence.create(sentence=line, source="cdd", progress="RAW")
    tokens = line.split(" ")
    total = len(tokens)
    for token in tokens:
        Token.create(
            token=token,
            index=index,
            sentenceId=sentence.id
        )
        index += len(token)

    


# with open("sentences.txt", 'w') as f:
#     for line in texts:
#         line = line.strip()

#         Sentence.create(
#             sentence=line,
#             source="cdd",
#             progress="RAW"
#         )

#         f.write(line)
#         f.write('.\n')
print("done")





