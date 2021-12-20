import pathlib
import numpy as np
from numpy.core.fromnumeric import prod

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
data = np.genfromtxt(path+'/data{}.csv'.format("_test" if test_data else ""), dtype=str)
data = np.array([list(row) for row in data], dtype=int)
# print(data)


print("###### TASK 1 ######")
def is_low(x,y):
    c1 = x != 0 and data[x,y] >= data[x-1,y]
    c2 = y != 0 and data[x,y] >= data[x,y-1]
    c3 = x != data.shape[0]-1 and data[x,y] >= data[x+1,y]
    c4 = y != data.shape[1]-1 and data[x,y] >= data[x,y+1]
    return not (c1 or c2 or c3 or c4)
risk = sum([1 + data[x,y] for x in range(data.shape[0]) for y in range(data.shape[1]) if is_low(x,y)])
print("Risk: ", risk)


print("###### TASK 2 ######")
basin_counter = 0
basins = np.zeros(data.shape, dtype=np.uint16)
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        if data[x,y] != 9:
            if x != 0 and basins[x-1,y] != 0: 
                basins[x,y] = basins[x-1,y]
                if y != 0 and basins[x,y-1] != 0 and basins[x,y-1] != basins[x,y]:
                    basins[basins==basins[x,y-1]] = basins[x,y]
            elif y != 0 and basins[x,y-1] != 0:
                basins[x,y] = basins[x,y-1]
            else:
                basin_counter += 1
                basins[x,y] = basin_counter
u, count = np.unique(basins, return_counts=True)
risk = prod(sorted(count[1:])[-3:])
print("Risk: ", risk)
