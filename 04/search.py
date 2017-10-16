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
               "WHERE person.name LIKE ? GROUP BY person.name", ("%{}%".format(searchedName),))

composerNames = []

for row in cursor:
    composerNames.append(row)

d = {"name": searchedName, "searched names": composerNames, "searched names size" : len(composerNames) }
json.dump(d, sys.stdout, indent=4)
