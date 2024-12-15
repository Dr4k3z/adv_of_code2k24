import sys
sys.path.append('..')
import re
import numpy as np
from utils import execution_time,save_output

class Machine:
    def __init__(self,A,B):
        self.buttonA = (A[0],A[1])
        self.buttonB = (B[0],B[1])

    def __str__(self):
        return f'Button A: {(self.buttonA)}   Button B: {self.buttonB}'

    @property
    def buttons(self):
        return self.buttonA,self.buttonB

def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)')
    matches = pattern.findall(content)
    
    machines = []
    prizes = []
    for match in matches:
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = map(int, match)
        
        machines.append(Machine((button_a_x,button_a_y),(button_b_x,button_b_y)))
        prizes.append((prize_x,prize_y))

    return machines,prizes

def part1():
    machines,prizes = parse_file('input.txt')
    total = 0
    lag = 10000000000000
    price = np.array([3,1])
    for m,p in zip(machines,prizes):
        A = np.array([m.buttonA,m.buttonB]).T
        b = np.array(p)+lag

        res = np.linalg.solve(A,b)
        res = np.array([int(x) for x in res])
        if np.all(A @ res == b):
            total += np.dot(price,res)
            #print(f'Reaching prize {p} took {np.sum(price * np.round(res))}')

    print(f'Total spent to reach all possible prizes: {int(total)}')

def part2():
    machines,prizes = parse_file('input.txt')
    total = 0
    lag = 10000000000000
    price = np.array([3,1])
    for m,p in zip(machines,prizes):
        A = np.array([m.buttonA,m.buttonB]).T
        b = np.array(p)+lag

        res = np.linalg.solve(A,b)
        res = np.array([int(x) for x in res])
        if np.all(A @ res == b):
            total += np.dot(price,res)
            #print(f'Reaching prize {p} took {np.sum(price * np.round(res))}')

    print(f'Total spent to reach all possible prizes: {int(total)}')

if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])