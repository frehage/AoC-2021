import pathlib
import numpy as np

test_data = 0

original_pattern = ""
injections = dict()

path = str(pathlib.Path(__file__).parent.resolve())
with open(path+"/data{}.csv".format("_test" if test_data else ""), 'r') as file:
    lines = file.read().splitlines()
    original_pattern = lines[0]
    for line in lines[2:]:
        injections[line[:2]] = line[6]
print("Pattern:", original_pattern)
# for pair, injection in injections.items(): print(pair, "->", injection)


print("###### TASK 1 ######")
steps = 10
pattern = original_pattern
for s in range(steps):
    next_pattern = pattern[0] + "".join([injections.get(pattern[i-1]+pattern[i], "") + pattern[i] for i in range(1,len(pattern))])
    pattern = next_pattern
pattern_array =np.array(list(pattern)) 
values, counts = np.unique(pattern_array, return_counts=True)
answer = max(counts)-min(counts)
print("Answer: ", answer)



print("###### TASK 2 ######")
steps = 40
pattern = original_pattern
pairs = dict()
for i in range(1,len(pattern)):
    pairs[pattern[i-1:i+1]] = pairs.get(pattern[i-1:i+1],0) + 1
for _ in range(steps):
    next = dict()
    for pair, count in pairs.items():
        if injection := injections.get(pair, ""):
            next[pair[0]+injection] = next.get(pair[0]+injection,0) + count
            next[injection+pair[1]] = next.get(injection+pair[1],0) + count
        else:
            next[pair] = next.get(pair,0) + count
    pairs = next
counts = {pattern[0]: 1, pattern[-1]: 1}
for pair, count in pairs.items():
    for i in range(2):
        counts[pair[i]] = counts.get(pair[i],0) + count
answer = (max(counts.values())-min(counts.values()))//2
print("Answer: ", answer)