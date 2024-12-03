import re

"""
    I hate regex
"""

def part1():
    lines = []
    with open('input.txt') as file:
        for line in file:
            lines.append(line.strip())

    total = 0
    for line in lines:
        splitted = line.split('mul(')

        for split in splitted:
            pattern = r"^(\d{1,3}),(\d{1,3})\)"
            match = re.match(pattern, split)

            if match:
                num1,num2 = match.groups()
                #print(f"{num1} * {num2} = {int(num1) * int(num2)}")
                total += int(num1) * int(num2)

    print(f'Total = {total}')

def part2(filename='input.txt'):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())

    total = 0
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    flag = True

    for line in lines:

        instructios = re.findall(pattern, line)
        for inst in instructios:
            match inst[0]:
                case "do()":
                    flag = True
                case "don't()":
                    flag = False
                case _ if flag:
                    total += int(inst[1]) * int(inst[2])

    print(f'Total = {total}')

if __name__=='__main__':
    part1()
    part2(filename='input.txt')