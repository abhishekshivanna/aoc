def main():
    with open('input') as fp:
        return sum([(int(line)/3) - 2 for line in fp])

if __name__ == '__main__':
    print(main())
