output = 19690720
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
    currPos = 0
    while codes[currPos] != EXIT and currPos < len(codes):
        if codes[currPos] == ADD:
            performAdd(codes[currPos+1], codes[currPos+2], codes[currPos+3], codes)
            currPos += 4
        if codes[currPos] == MUL:
            performMul(codes[currPos+1], codes[currPos+2], codes[currPos+3], codes)
            currPos += 4

def runMain(codes):
    backup = codes[:]
    for noun in range(100):
        for verb in range(100):
            codes = backup[:]
            print(noun, verb)
            codes[1] = noun
            codes[2] = verb
            main(codes)
            if codes[0] == output:
                return (noun, verb)

if __name__ == '__main__':
    codes = getInput("input")
    noun, verb = runMain(codes)
    print(100 * noun + verb)

