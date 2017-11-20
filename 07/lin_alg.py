import re
from collections import Counter

from numpy import linalg, loadtxt, hsplit, matrix, append

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

for line in open('equations.txt', 'r'):
    parsed = r.match(line)
    left_part = list(filter(None, parsed.group(1).split(' ')))
    right_part = int(parsed.group(2))
    sign = 1
    number = 1
    row_matrix = []

    for p in left_part:
        if p == '+' or p == '-':
            sign = -1 if p == '-' else 1
        elif p.isnumeric():
            number = int(p)
        else:
            print(p, sign * number)
            aa[p] = sign * number
print(aa)
