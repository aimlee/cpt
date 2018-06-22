import re
import numpy as np
import scipy.spatial.distance as cs

file_obj = open('sentences.txt', 'r')

lines = []
for line in file_obj:
        s = re.split('[^a-z]', line.lower())
        s = [x for x in s if x]
        lines.append(s)
file_obj.close()
a = set()
for i in lines:
    for j in i:
        a.add(j)
n = len(lines)
d = len(a)

matrix = np.zeros((n, d))


for indexLine, valueLine in enumerate(lines):
    for indexSet, valueSet in enumerate(a):
        matrix[indexLine, indexSet] = valueLine.count(valueSet)
dist = np.argsort([cs.cosine(matrix[0], row) for row in matrix[1:]]) + 1
file_w = open('submission-1.txt', 'w')
string = str(dist[0]) + ' ' + str(dist[1])
file_w.write(string)
file_w.close()
