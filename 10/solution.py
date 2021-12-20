import pathlib
import numpy as np
from numpy.core.fromnumeric import prod

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
data = np.genfromtxt(path+'/data{}.csv'.format("_test" if test_data else ""), dtype=str)
# print(data)

endings = [')', ']', '}', '>']
start = {')': '(', ']': '[', '}': '{', '>': '<'}


print("###### TASK 1 ######")
points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
total = 0
for row in data:
    stack = "."
    for c in row:
        if c in endings:
            if stack[-1] == start[c]: 
                stack = stack[:-1]
            else: 
                total += points[c]
                break
        else: stack += c
print("Total: ", total)


print("###### TASK 2 ######")
points = { '(': 1, '[': 2, '{': 3, '<': 4 }
scores = []
for row in data:
    stack = "."
    for c in row:
        if c in endings:
            if stack[-1] == start[c]: 
                stack = stack[:-1]
            else: 
                stack = ""
                break
        else: stack += c
    if len(stack) > 1:
        score = 0
        for c in reversed(stack[1:]):
            score = score * 5 + points[c]
        scores.append(score)
print("Total: ", sorted(scores)[len(scores)//2])