import pathlib
import numpy as np

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
with open(path+"/data{}.csv".format("_test" if test_data else ""), 'r') as file:
    lines = file.read().splitlines()
    cavern = np.empty((len(lines), len(lines[1])), dtype=int)
    for i in range(len(lines)):
        cavern[i,:] = list(map(int,lines[i]))
print(cavern)

def a_star(grid, source=(0,0), _goal=False):
    
    goal = _goal if _goal else (grid.shape[0]-1, grid.shape[1]-1)

    def get_neighbors(n):
        candicates = [(n[0]-1,n[1]), (n[0]+1,n[1]), (n[0],n[1]-1), (n[0],n[1]+1)]
        return [v for v in candicates if 0 <= v[0] < grid.shape[0] and 0 <= v[1] < grid.shape[1]]
    open = set([source])
    visited = set([])
    g = {source: 0}
    def h(v): return abs(v[0]-goal[0]) + abs(v[1]-goal[1])
    print(h(source), h(goal))
    while len(open) > 0:
        n = None
        for v in open:
            if n == None or g[v] < g[n]:
                n = v
        open.remove(n)
        visited.add(n)

        if n == goal: 
            break

        for m in get_neighbors(n):
            if m not in open and m not in visited:
                open.add(m)
                g[m] = g[n] + grid[m]
    print(len(visited), grid.shape)
    return g[goal]

print("###### TASK 1 ######")
answer = a_star(cavern)
print("Answer: ", answer)

print("###### TASK 2 ######")
cavern_large = np.tile(cavern,(5,5))
size = len(cavern)
for i in range(len(cavern_large)):
    extra_cost = i//size
    cavern_large[:,i] += extra_cost
    cavern_large[i,:] += extra_cost 
cavern_large = (cavern_large - 1) % 9 + 1
# print(cavern_large)
answer = a_star(cavern_large)
print("Answer: ", answer)