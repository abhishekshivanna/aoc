def getInput(filename):
    wire = []
    with open(filename) as fp:
        for line in fp:
            wire.append([(i[0], int(i[1:])) for i in line.split(',')])
    return wire

def traceWire(wire):
    curPos = (0, 0)
    path = set()
    for direction, step in wire:
        if direction == "R":
            for i in range(step):
                curPos = (curPos[0]+1, curPos[1])
                path.add(curPos)
        if direction == "L":
            for i in range(step):
                curPos = (curPos[0]-1, curPos[1])
                path.add(curPos)
        if direction == "U":
            for i in range(step):
                curPos = (curPos[0], curPos[1]+1)
                path.add(curPos)
        if direction == "D":
            for i in range(step):
                curPos = (curPos[0], curPos[1]-1)
                path.add(curPos)
    return path

def getManhattanDistance(y, x):
    return abs(0 - x) + abs(0 - y)

def getClosestIntersectionDist(path1, path2):
    intersections = path1.intersection(path2)
    return min([getManhattanDistance(i[0], i[1]) for i in intersections])

if __name__ == '__main__':
    wire1, wire2 = getInput('input')
    path1 = traceWire(wire1)
    path2 = traceWire(wire2)
    dist = getClosestIntersectionDist(path1, path2)
    print(dist)