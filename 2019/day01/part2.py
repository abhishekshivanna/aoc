def fuel(mass):
    totalfuel = 0
    fuelMass = (int(mass)/3) - 2
    while fuelMass > 0 :
        totalfuel += fuelMass
        fuelMass = (int(fuelMass)/3) - 2
    return totalfuel

def main():
    with open('input') as fp:
        return sum([fuel(line) for line in fp])

if __name__ == '__main__':
    print(main())
