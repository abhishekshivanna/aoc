EXIT = 99
ADD = 1
MUL = 2

def getInput(filename):
    with open(filename) as fp:
        return [int(i) for i in fp.read().split(',')]

def performAdd(arg1Pos, arg2pos, resultPos, codes):
    codes[resultPos] = codes[arg1Pos] + codes[arg2pos]

def performMul(arg1Pos, arg2pos, resultPos, codes):
    codes[resultPos] = codes[arg1Pos] * codes[arg2pos]


def main(codes):
    EXIT = 99
    ADD = 1
    MUL = 2
    currPos = 0
    while codes[currPos] != EXIT and currPos < len(codes):
        if codes[currPos] == ADD:
            performAdd(codes[currPos+1], codes[currPos+2], codes[currPos+3], codes)
            currPos += 4
        if codes[currPos] == MUL:
            performMul(codes[currPos+1], codes[currPos+2], codes[currPos+3], codes)
            currPos += 4
    print(codes[0])

if __name__ == '__main__':
    codes = getInput("input")
    codes[1] = 12
    codes[2] = 2
    main(codes)
