with open('3/data.txt', 'r') as f:
    lines = f.read().splitlines()
    n = len(lines)
    bits = len(lines[0])

    # Task 1
    c = [0] * bits
    for line in lines:
        for i in range(bits):
            c[i] += int(line[i])
    gamma = ''.join([str(x*2//n) for x in c])
    epsilon = ''.join([str(int(x=='0')) for x in gamma])
    print("Answer:", int(gamma,2)*int(epsilon,2))

    # Task 2
    olines = lines
    clines = lines.copy()
    for i in range(bits):
        x = sum([int(line[i]) for line in olines])*2//len(olines)
        olines = list(filter(lambda line: int(line[i]) == x, olines))
    for i in range(bits):
        if (len(clines) == 1): break
        x = int(sum([int(line[i]) for line in clines])*2/len(clines)<1)
        clines = list(filter(lambda line: int(line[i]) == x, clines))

    print("Answer:", int(olines[0],2) * int(clines[0],2))