with open("input") as fp:
    code = [line.split() for line in fp]


def part1(code):
    ip = 0
    acc = 0
    seen = set()

    def doop(ip, acc, op, arg):
        if op == "nop":
            ip += 1
        if op == "acc":
            acc += int(arg)
            ip += 1
        if op == "jmp":
            ip += int(arg)
        # print(ip, acc)
        return ip, acc

    stops = False
    while True:
        if ip in seen:
            break
        seen.add(ip)
        if ip == len(code):
            stops = True
            break
        op = code[ip][0]
        arg = code[ip][1]
        ip, acc = doop(ip, acc, op, arg)
    return (acc, stops)


def part2():
    acc = 0
    for ip in range(len(code)):
        if code[ip][0] == "jmp":
            code[ip][0] = "nop"
        elif code[ip][0] == "nop":
            code[ip][0] = "jmp"
        acc, stops = part1(code)
        if stops:
            print(acc)
        if code[ip][0] == "jmp":
            code[ip][0] = "nop"
        elif code[ip][0] == "nop":
            code[ip][0] = "jmp"


print(part1(code)[0])
part2()
