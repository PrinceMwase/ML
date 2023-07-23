import os
from eloquent import DatabaseManager, Model
from dotenv import load_dotenv
import csv

load_dotenv() # take environment variables from .env.
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
os.getenv
config = {
    "mysql": {
        "driver": os.getenv("DRIVER", 'mysql'),
        "host": os.getenv("HOST", 'localhost'),
        "database": os.getenv("DATABASE", 'ml'),
        "user": os.getenv("USER", 'ml'),
        "password": os.getenv("PASSWORD", 'password'),
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
        if (counter < 5000):
            counter += 1
            continue
        if (counter > 6000):
            break
        index = 0
        line = line.strip()
        sentence = Sentence.create(sentence=line, source="cdd", progress="RAW")
        tokens = line.split(" ")
        total = len(tokens)

        for token in tokens:
            tk = Token.create(
                token=token,
                index=index,
                sentenceId=sentence.id
            )

            index += len(token) + 1

        counter += 1
        print(counter)


print("done")




