with open('2/data.txt', 'r') as f:
    
    lines = f.read().splitlines()

    # Task 1
    x=y=0
    for line in lines:
        if line[0] == 'f':
            x +=  int(line[-1])
        elif line[0] == 'd':
            y += int(line[-1])
        else:
            y -= int(line[-1])
    print("Task 1:",  x*y)

    # Task 2
    x=y=aim=0
    for line in lines:
        if line[0] == 'f':
            x +=  int(line[-1])
            y += int(line[-1]) * aim
        elif line[0] == 'd':
            aim += int(line[-1])
        else:
            aim -= int(line[-1])
    print("Task 2:",  x*y)