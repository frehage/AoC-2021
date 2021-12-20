import pathlib
import numpy as np

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
data = np.genfromtxt(path+'/data{}.csv'.format("_test" if test_data else ""), delimiter=' ', dtype=str)
# print(data)


print("###### TASK 1 ######")
output = data[:,11:].ravel()
relevant_output = np.array([n for n in output if len(n) <= 4 or len(n) == 7])
print("Answer: ", len(relevant_output))


print("###### TASK 2 ######")
total = 0
for display in data:
    digits = [d for d in display[:10]]
    output = [d for d in display[11:]]
 
    def is_subset(subs, supers):
        return all(y in supers for y in subs)

    # identify a 1, 4 and 6, which is required to deduct the rest.    
    one     = [x for x in digits if len(x) == 2][0]
    four    = [x for x in digits if len(x) == 4][0]
    six     = [x for x in digits if len(x) == 6 and not is_subset(one, x)][0]

    def convert(d): 
        if len(d) == 2: return 1
        elif len(d) == 3: return 7
        elif len(d) == 4: return 4
        elif len(d) == 5: 
            if is_subset(one, d): return 3
            elif is_subset(d, six): return 5
            else: return 2
        elif len(d) == 6: 
            if not is_subset(one, d): return 6
            elif is_subset(four, d): return 9
            else: return 0
        else: return 8
            
    print("".join([str(convert(d)) for d in output]))
    total += int("".join([str(convert(d)) for d in output]))

print("Answer: ", total)