import pathlib
import numpy as np

test_data = 0

path = str(pathlib.Path(__file__).parent.resolve())
with open(path+"/data{}.csv".format("_test"+str(test_data) if test_data != 0 else ""), 'r') as file:
    transmissions = file.read().splitlines()
# for trans in transmissions: print(trans)

def h2b(n):
    return bin(int(n, 16))[2:].zfill(len(n)*4)
def processPackage(trans):
    package = {'version': int(trans[:3],2)}
    if trans[3:6] == '100': 
        n = ""
        i = 11
        while trans[i-5] != '0': 
            n += trans[i-4:i]
            i += 5
        n += trans[i-4:i]
        package["type"] = int(trans[3:6],2)
        package["value"] = int(n,2)
    else:
        package["type"] = int(trans[3:6],2)
        package["subs"] = []
        if trans[6] == '1':
            subs = int(trans[7:18],2)
            # print('operator', int(trans[:3],2), " subs: ", subs, trans)
            i = 18
            for s in range(subs):
                j, p = processPackage(trans[i:])
                i += j
                package["subs"].append(p)
        else:
            bits = int(trans[7:22],2)
            # print('operator', int(trans[:3],2), " bits: ",bits, trans)
            i = 22
            while i < 22 + bits:
                j, p = processPackage(trans[i:])
                i += j
                package["subs"].append(p)
    return i, package

print("###### TASK 1 ######")
for t in transmissions:
    transmission = h2b(t)
    _, package = processPackage(transmission)
    answer = sum([int(r[0]) for r in str(package).split("'version': ")[1:]])
    print("Answer: ", answer)

print("###### TASK 2 ######")
def evaluatePackage(package):
    if package["type"] == 0:
        return sum([evaluatePackage(p) for p in package["subs"]])
    elif package["type"] == 1:
        return np.prod([evaluatePackage(p) for p in package["subs"]])
    elif package["type"] == 2:
        return min([evaluatePackage(p) for p in package["subs"]])
    elif package["type"] == 3:
        return max([evaluatePackage(p) for p in package["subs"]])
    elif package["type"] == 4:
        return package["value"]
    elif package["type"] == 5:
        return int(evaluatePackage(package["subs"][0]) > evaluatePackage(package["subs"][1]))
    elif package["type"] == 6:
        return int(evaluatePackage(package["subs"][0]) < evaluatePackage(package["subs"][1]))
    elif package["type"] == 7:
        return int(evaluatePackage(package["subs"][0]) == evaluatePackage(package["subs"][1]))
for t in transmissions:
    transmission = h2b(t)
    _, package = processPackage(transmission)
    answer = evaluatePackage(package)
    print("Answer: ", answer)
