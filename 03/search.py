import json
import sqlite3
import sys

total = len(sys.argv)

if total != 2:
    raise Exception("Incorrect number of arguments, need 1")

searchedName = sys.argv[1]

connection = sqlite3.connect('scorelib.dat')
cursor = connection.cursor()
cursor.execute("SELECT person.name, score.name FROM score JOIN score_author JOIN person "
               "ON score.id = score_author.score AND score_author.composer = person.id "
               "WHERE person.name LIKE ? ORDER BY person.name", ("%{}%".format(searchedName),))

scores = {}

for row in cursor:

    if row[0] not in scores:
        scores[row[0]] = []

    scores[row[0]].append(row[1])

json.dump(scores, sys.stdout, indent=4)
