import pathlib
import numpy as np

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
data = np.genfromtxt(path+'/data{}.csv'.format("_test" if test_data else ""), dtype=str)
data = np.array([list(map(int, d)) for d in data], int)
def printGrid(): [print("".join(list(map(str,d)))) for d in grid[1:-1,1:-1]]; print("")



print("###### TASK 1 ######")
grid = np.zeros([len(data)+2, len(data[0])+2], int)
grid[1:-1,1:-1] = data
printGrid()

steps = 100
size = len(data)
def evalFlashes(xrange,yrange):
    for x in xrange:
        for y in yrange:
            if 0 < x < size+1 and 0 < y < size+1 and grid[x,y] < 10: 
                grid[x,y] += 1
                if grid[x,y] == 10: evalFlashes(range(x-1, x+2), range(y-1, y+2))
# evalFlashes(range(1, size+1),range(1, size+1))

total = 0
for s in range(steps):
    evalFlashes(range(len(grid)),range(len(grid)))
    count = len(grid[grid==10])
    total += count
    grid[grid==10] = np.zeros(count)
    # printGrid()
answer = total
print("Answer: ", answer)



print("###### TASK 2 ######")
grid = np.zeros([len(data)+2, len(data[0])+2], int)
grid[1:-1,1:-1] = data
printGrid()

step = 0
while step < 500:
    step += 1
    evalFlashes(range(len(grid)),range(len(grid)))
    count = len(grid[grid==10])
    grid[grid==10] = np.zeros(count)
    if count == size**2: break
printGrid()
answer = step
print("Answer: ", answer)