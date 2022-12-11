from eloquent import DatabaseManager, Model
import csv


# config = {
#     "mysql": {
#         "driver": "mysql",
#         "host": "localhost",
#         "database": "ml",
#         "user": "admin",
#         "password": "password",
#         "prefix": "",
#     }
# }
# PV2BJF9qc7ijhfu

config = {
    "mysql": {
        "driver": "mysql",
        "host": "sitbecmw.com",
        "database": "sitbecmw_ml",
        "user": "sitbecmw_ml",
        "password": "PV2BJF9qc7ijhfu",
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

counter = 1

with db.transaction():
    for line in texts:
        if (counter < 201):
            counter += 1
            continue
        if (counter > 400):
            break
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

        counter += 1
        print(counter)


print("done")




