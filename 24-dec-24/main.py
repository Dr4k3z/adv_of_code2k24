import sys
sys.path.append('..')
import re
from collections import defaultdict,deque
from itertools import combinations
from utils import read_input

def parse_input(data):
    variables = defaultdict(int)
    operations = []

    for line in data:
        if '->' in line:
            operations.append(line)
        elif ':' in line:
            var, value = line.split(': ')
            variables[var] = int(value)

    return variables, operations

def find_string(gates, operations, output=None):
    func_dict = {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR' : lambda x, y: x ^ y
    }

    queue = deque()
    for operation in operations:
        # very very ugly
        if output:
            inputs,_ = operation.split(' -> ')
        else:
            inputs,output = operation.split(' -> ')

        gate1,gate2 = inputs[0:3],inputs[-3:]

        operator = func_dict[re.search(r'AND|OR|XOR', inputs).group()]

        if (gate1 not in gates) or (gate2 not in gates):
            queue.append((gate1,gate2,operator,output))
            continue
        gates[output] = operator(gates[gate1], gates[gate2])

    while queue:
        gate1,gate2,operator,output = queue.popleft()
        if (gate1 not in gates) or (gate2 not in gates):
            queue.append((gate1,gate2,operator,output))
            continue
        gates[output] = operator(gates[gate1], gates[gate2])

    final_nums = []
    for key in gates.keys():
        if 'z' in key:
            num = int(re.search(r'\d+', key).group())
            final_nums.append((num, gates[key]))

    final_nums = sorted(final_nums, key=lambda x: x[0], reverse=True)
    ans = [str(f[1]) for f in final_nums]
    return int(''.join(ans),2)

def part1():
    data = read_input('input.txt')

    gates, operations = parse_input(data)
    return find_string(gates, operations)

def part2():
    data = read_input('example3.txt')

    gates, operations = parse_input(data)
    outputs = [op.split(' -> ')[1] for op in operations]

    x,y = '',''
    for key,val in gates.items():
        if 'x' in key:
            x += str(val)
        elif 'y' in key:
            y += str(val)

    target = int(x,2)+int(y,2)

    for a, b, c, d in combinations(outputs, 4):
        gates_copy = gates.copy()
        gates_copy[a], gates_copy[b], gates_copy[c], gates_copy[d] = gates_copy[d], gates_copy[c], gates_copy[b], gates_copy[a]
        result = find_string(gates_copy, operations)
        if result == target:
            print(f"Swapping {a}, {b}, {c}, and {d} results in the target value.")
            return
    print("No combination of swaps results in the target value.")
    


if __name__ == "__main__":
    part2()