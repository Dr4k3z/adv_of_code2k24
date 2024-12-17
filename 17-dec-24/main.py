import sys
sys.path.append('..')
import re
from utils import read_input,execution_time,save_output


data = read_input('input.txt')
data = '\n'.join(data)
registers = {'A' : 0, 'B' : 0, 'C' : 0}

numbers = list(map(int, re.findall(r'\d+', data)))

registers['A'] = numbers[0]
registers['B'] = numbers[1]
registers['C'] = numbers[2]
program = numbers[3:]

def combos(registers):
    return {
        0 : 0,
        1 : 1,
        2 : 2,
        3 : 3,
        4 : registers['A'],
        5 : registers['B'],
        6 : registers['C']
    }

def adv(x):
    registers['A'] = int(registers['A']/(2**combos(registers)[x]))

def bxl(x):
    registers['B'] = registers['B'] ^ x

def bst(x):
    registers['B'] = combos(registers)[x] % 8
    
def jnz(x):
    global inst_pointer,flag
    if registers['A'] == 0:
        return
    inst_pointer = x
    flag = False

def bxc(x):
    registers['B'] = registers['B'] ^ registers['C']

def out(x) -> int:
    return combos(registers)[x] % 8

def bdv(x):
    registers['B'] = int(registers['A']/(2**combos(registers)[x]))

def cdv(x):
    registers['C'] = int(registers['A']/(2**combos(registers)[x]))

def program_output():
    global inst_pointer, flag
    instructions = {
            0 : adv,
            1 : bxl,
            2 : bst,
            3 : jnz,
            4 : bxc,
            5 : out,
            6 : bdv,
            7 : cdv
        }

    inst_pointer = 0
    output = ''
    while inst_pointer < len(program):
        flag = True

        inst = instructions[program[inst_pointer]]
        res = inst(program[inst_pointer+1])

        if flag:
            inst_pointer += 2

        if res is not None:
            output += str(res)+','

        #print(f'Registers = {registers}')

    output = [int(c) for c in output[:-1].split(',')]
    return output

def part2():
    '''
        I haven't got it.
        Why the f does it work?
    '''
    candidates = [0]    
    for length in range(1, len(program) + 1):
            out = []

            for num in candidates:
                # try all 3-bit combinations
                for offset in range(2**3):
                    a = (2**3) * num + offset
                    registers['A'] = a

                    if program_output() == program[-length:]:
                        out.append(a)

            candidates = out

    return min(candidates)

if __name__ == "__main__":
    #print(f'Part 1: {program_output()}')
    #print(f'Part 2: {part2()}')

    part1_time = execution_time(program_output)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])