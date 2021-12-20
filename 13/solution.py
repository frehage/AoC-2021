import pathlib
#import numpy as np

test_data = 0

points = set()
folds = []
path = str(pathlib.Path(__file__).parent.resolve())
with open(path+"/data{}.csv".format("_test" if test_data else ""), 'r') as file:
    for line in file.read().splitlines():
        if line.startswith("fold"): 
            folds.append((line[11], int(line[13:])))
        elif line:
            points.add(tuple(map(int,line.split(","))))
# for p in points: print(p)
# for f in folds: print(f)

print("###### TASK 1 ######")
def tf(x, f):
    return x if x <= f else 2*f - x
def fold(f):
    for p in list(points):
        np = (p[0] if f[0] == 'y' else tf(p[0],f[1]), p[1] if f[0] == 'x' else tf(p[1],f[1]))
        if not p == np:
            points.remove(p)
            points.add(np)
fold(folds[0])
answer = len(points)
print("Answer: ", answer)



print("###### TASK 2 ######")
for f in folds[1:]: fold(f)
answer = len(points)
for p in points: print(p)
print("Answer: ", answer)

grid = []
for y in range(max(points, key=lambda p: p[1])[1]+1):
    grid.append([ '#' if (x,y) in points else '.' for x in range(max(points, key=lambda p: p[0])[0]+1)])
for p in grid: print("".join(p))