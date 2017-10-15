import sys

total = len(sys.argv)

if total != 2:
    raise Exception("Incorrect number of arguments, need 1")

printNumber = int(sys.argv[1])

# select ... from person join score_authors on person.id = score_author.composer ... where print.id = ?
