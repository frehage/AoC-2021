import numpy as np
test_data = 0
data = np.genfromtxt('6/data{}.csv'.format("_test" if test_data else ""), delimiter=',', dtype=int)

fish_count = np.zeros(9,dtype=np.ulonglong)
for x in data: fish_count[x] += 1
print(fish_count, np.sum(fish_count))

days = 256
for day in range(days):
    fish_count = np.roll(fish_count,-1)
    fish_count[6] += fish_count[8]
    print(fish_count, np.sum(fish_count))

print("Final amount: ", np.sum(fish_count))

