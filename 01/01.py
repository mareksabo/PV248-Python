import re
from collections import Counter

r = re.compile(r"Composer: (.*)")
r2 = re.compile(r"Composition Year: (.*)")
dict = Counter()

for line in open('scorelib.txt', 'r'):
    composer = r.match(line)
    century = r2.match(line)
    if composer is not None:
        dict[composer.group(1)] += 1

for i,j in dict.items():
    print("{}: {}".format(i,j))

