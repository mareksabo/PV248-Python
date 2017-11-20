import json
import sqlite3
import sys

total = len(sys.argv)

if total != 2:
    raise Exception("Incorrect number of arguments, need 1")

printId = sys.argv[1]

connection = sqlite3.connect('scorelib.dat')
cursor = connection.cursor()
cursor.execute("SELECT person.name FROM print JOIN edition JOIN score JOIN score_author JOIN person "
               "ON print.edition = edition.id "
               "AND edition.score = score.id "
               "AND score.id = score_author.score "
               "AND score_author.composer = person.id "
               "WHERE print.id = ?", printId)

composers = []

for row in cursor:
    composers.append(row)

d = {"print": printId, "composers": composers}
json.dump(d, sys.stdout, indent=4)
