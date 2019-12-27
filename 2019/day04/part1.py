START = 138241
END = 674034


def ruleIncrOnly(num):
    if num == int("".join(sorted(str(num)))):
        return True
    return False

def ruleAdjSame(num):
    for i in range(10):
        if str(i) * 2 in str(num):
            return True
    return False

def main():
    count = 0
    for i in range(START, END):
        if ruleAdjSame(i) and ruleIncrOnly(i):
            count += 1
    return count

if __name__ == '__main__':
    print(main())