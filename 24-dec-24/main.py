import sys
sys.path.append('..')
import re
from collections import defaultdict,deque
from itertools import combinations
from utils import read_input,execution_time,save_output

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

def part1():
    data = read_input('input.txt')

    gates, operations = parse_input(data)
    
    func_dict = {
            'AND': lambda x, y: x & y,
            'OR': lambda x, y: x | y,
            'XOR' : lambda x, y: x ^ y
        }

    queue = deque()
    for operation in operations:
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
    return [str(f[1]) for f in final_nums]

if __name__ == "__main__":
    part1_time = execution_time(part1)
    save_output(new_row=[part1_time,'N/A'])