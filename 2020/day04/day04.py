import re


def parseline(line):
    di = {}
    parts = line.split()
    for part in parts:
        k, v = part.split(":")
        di[k] = v
    return di


def read():
    with open("input") as fp:
        passports = []
        cur = ""
        for line in fp:
            line = line.strip()
            if not line:
                passports.append(parseline(cur.strip()))
                cur = ""
                continue
            cur = cur + " " + line
        passports.append(parseline(cur.strip()))
    return passports


# FML
without_cid = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: len(re.findall("^\\d+in$|^\\d+cm$", x)) == 1 and
    (('cm' in x and (150 <= int(x[:-2]) <= 193))
     or ('in' in x and (59 <= int(x[:-2]) <= 76))),
    'hcl': lambda x: len(re.findall("^#[a-f0-9]{6}$", x)) == 1,
    'ecl': lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    'pid': lambda x: len(re.findall("^[0-9]{9}$", x)) == 1,
}


with_cid = dict(without_cid, **{'cid': lambda x: True})


def part1():
    valid = 0
    for p in read():
        if set(p.keys()) == set(with_cid.keys()) or \
                set(p.keys()) == set(without_cid.keys()):
            valid += 1
    print(valid)


def part2():
    valid = 0
    for p in read():
        if set(p.keys()) == set(with_cid.keys()) and\
                all([with_cid[k](p[k]) for k in p]):
            valid += 1
            continue
        if set(p.keys()) == set(without_cid.keys()) and\
                all([without_cid[k](p[k]) for k in p]):
            valid += 1
    print(valid)


part1()
part2()
