from collections import deque

window = 25
with open("input") as fp:
    lines = map(int, [line for line in fp])


def pairExists(target, d):
    D = sorted(d)
    left = 0
    right = window - 1
    while left < right:
        if D[left] + D[right] == target:
            return True
        elif D[left] + D[right] < target:
            left += 1
        else:
            right -= 1
    return False


def part1():
    i = window
    d = deque(lines[:window])
    while i < len(lines):
        target = lines[i]
        if pairExists(target, d):
            i += 1
            d.append(lines[i-1])
            d.popleft()
            continue
        else:
            return target


def slidingWindow(nums, winSize):
    i = 0
    nums = list(nums)
    while i + winSize < len(nums):
        yield nums[i:i+winSize]
        i += 1


def rangeExists(target, d):
    winSize = 2
    while winSize < len(d):
        for win in slidingWindow(d, winSize):
            if sum(win) == target:
                return True, win
        winSize += 1
    return False, d


def part2():
    i = window
    d = deque(lines[:window])
    target = part1()
    while i < len(lines):
        exists, range = rangeExists(target, d)
        if not exists:
            i += 1
            d.append(lines[i-1])
            d.popleft()
            continue
        else:
            print(min(range) + max(range))
            break


print(part1())
part2()
