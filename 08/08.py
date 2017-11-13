import re
from collections import Counter

from numpy import linalg, loadtxt, hsplit

orig = loadtxt('matrix.txt')

(height, width) = orig.shape

print(orig)

[a, b] = hsplit(orig, [3])

print('Matrix without right part:')
print(a)

D = linalg.det(a)

print('Determinant: ', D)

inverse = linalg.inv(a)

print('Inverse matrix:')
print(inverse)

solution = linalg.solve(a, b)
print('Solution:')
print(solution)

r = re.compile(r"(.*)[ ]*=[ ]*(.*)")
aa = Counter()
bb = []
for line in open('equations.txt', 'r'):
    parsed = r.match(line)
    bb.append(parsed.group(2))
    left_part = list(filter(None, parsed.group(1).split(' ')))
    sign = '+'
    number = 1
    for p in left_part:
        if p == '+' or p == '-':
            sign = p
        elif p.isnumeric():
            number = (int) p
        else:
            aa[p] = number
print(bb)