import pathlib
import numpy as np

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
data = np.genfromtxt(path+'/data{}.csv'.format("_test" if test_data else ""), dtype=str)
print(data)


print("###### TASK 1 ######")
answer = "Not Yet Implemented"
print("Answer: ", answer)



print("###### TASK 2 ######")
answer = "Not Yet Implemented"
print("Answer: ", answer)