task = 2
with open('5/data.txt', 'r') as f:
    vertical = []
    horizontal = []
    diagonal = []
    for row in f.read().splitlines():
        positions = [int(position) for part in row.split(' -> ') for position in part.split(',')]
        if positions[0] == positions[2]: vertical.append(positions)
        elif positions[1] == positions[3]: horizontal.append(positions)
        else: diagonal.append(positions)

    positions = {}
    for line in vertical:
        y = line[0]
        for x in range(min(line[1],line[3]),max(line[1],line[3])+1):
            name =  "{},{}".format(x,y)
            positions[name] = 1 + positions.get(name,0)
    for line in horizontal:
        x = line[1]
        for y in range(min(line[0],line[2]),max(line[0],line[2])+1):
            name =  "{},{}".format(x,y)
            positions[name] = 1 + positions.get(name,0)
    
    if task == 2:
        for line in diagonal:
            steps = abs(line[0]-line[2])
            x = line[1]
            y = line[0]
            for i in range(0, steps+1):
                name =  "{},{}".format(x,y)
                positions[name] = 1 + positions.get(name,0)
                x = x + 1 if line[1] < line[3] else x - 1
                y = y + 1 if line[0] < line[2] else y - 1

    overlaps = list(map(lambda x: x > 1, positions.values())).count(True)
    print("Answer:", overlaps)