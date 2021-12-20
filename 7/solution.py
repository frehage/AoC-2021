import pathlib
import numpy as np

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
data = np.genfromtxt(path+'/data{}.csv'.format("_test" if test_data else ""), delimiter=',', dtype=int)
# data = np.array([0,0,0,0,8])
print(len(data), data.max(), data.mean())

print("###### TASK 1 ######")
rendezvous_point = np.sort(data)[len(data)//2]
print("Rendezvous point: ", rendezvous_point)
fuel = abs(data - rendezvous_point)
print("Total fuel: ", fuel.sum())



print("###### TASK 2 ######")
triangular_sum = lambda x: x*(x+1)//2
fuel = {x:sum(triangular_sum(abs(data - x))) for x in range(data.min(), data.max()+1)}
rendezvous_point = min(fuel, key=fuel.get) # thought it would be "round(data.mean())" but something is fishy here...
print("Rendezvous point: ", rendezvous_point)
print("Total fuel: ", fuel[rendezvous_point])