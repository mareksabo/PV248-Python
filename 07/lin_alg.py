import re
from collections import Counter

from numpy import linalg, loadtxt, hsplit, matrix, array

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
final_lists = []
b = []

for line in open('equations.txt', 'r'):
    parsed = r.match(line)
    left_part = list(filter(None, parsed.group(1).split(' ')))
    right_part = int(parsed.group(2))
    b.append(right_part)

    sign = 1
    number = 1
    unknown_vars = Counter()

    for p in left_part:
        if p == '+' or p == '-':
            sign = -1 if p == '-' else 1
        elif p.isnumeric():
            number = int(p)
        else:
            print(p, sign * number)
            unknown_vars[p] = sign * number
    final_lists.append(list(unknown_vars.values()))

unknown_vars_names = list(unknown_vars.keys())

final_matrix = array(final_lists)
result = linalg.solve(final_matrix, b)

for i in range(0, len(result)):
    print("{} = {}".format(unknown_vars_names[i], result[i]))

