START = 138241
END = 674034


def ruleIncrOnly(num):
    if num == int("".join(sorted(str(num)))):
        return True
    return False

def ruleOnly2CharsAdjSame(num):
    selected = False
    for i in range(10):
        if str(i) * 2 in str(num) and not str(i) * 3 in str(num):
            selected = True
            break
    return selected

def main():
    count = 0
    for i in range(START, END):
        if ruleIncrOnly(i) and ruleOnly2CharsAdjSame(i):
            count += 1
    return count

if __name__ == '__main__':
    print(main())