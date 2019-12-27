def getInput(filename):
    wire = []
    with open(filename) as fp:
        for line in fp:
            wire.append([(i[0], int(i[1:])) for i in line.split(',')])
    return wire

def traceWire(wire):
    curPos = (0, 0)
    steps = 0
    path = dict()
    for direction, step in wire:
        if direction == "R":
            for i in range(step):
                curPos = (curPos[0]+1, curPos[1])
                steps += 1
                if not curPos in path:
                    path[curPos] = steps
        if direction == "L":
            for i in range(step):
                curPos = (curPos[0]-1, curPos[1])
                steps += 1
                if not curPos in path:
                    path[curPos] = steps
        if direction == "U":
            for i in range(step):
                curPos = (curPos[0], curPos[1]+1)
                steps += 1
                if not curPos in path:
                    path[curPos] = steps
        if direction == "D":
            for i in range(step):
                curPos = (curPos[0], curPos[1]-1)
                steps += 1
                if not curPos in path:
                    path[curPos] = steps
    return path

def getMinStepSumToIntersections(path1, path2):
    intersections = set(path1.keys()).intersection(set(path2.keys()))
    return min([path1[point] + path2[point] for point in intersections])


if __name__ == '__main__':
    wire1, wire2 = getInput('input')
    path1 = traceWire(wire1)
    path2 = traceWire(wire2)
    steps = getMinStepSumToIntersections(path1, path2)
    print(steps)
    