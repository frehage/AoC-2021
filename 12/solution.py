# max_exceptions = 0 for task 1, max_exceptions = 0 for task 2
max_exceptions = 1
def explore(x, next, exceptions = 0, visited = ['end']) -> int :
    count = int('end' in next)
    for cave in next:
        e = exceptions + int(cave.islower() and cave in visited)
        if cave != 'end' and e <= max_exceptions:
            count += explore(cave, targets[cave], e, visited+[cave])
    return count
with open('data.txt', 'r') as f:
    caves = set()
    targets = dict()
    for row in f.read().splitlines():
        passage = row.split('-')
        for cave in passage:
            if not cave in caves:
                targets[cave] = []
                caves.add(cave)
        targets[passage[0]].append(passage[1])
        targets[passage[1]].append(passage[0])
    targets.pop("end")
    targets = {cave: list(filter(lambda target: not target == 'start', targets[cave])) for cave in targets}
    print(explore("", targets['start']))