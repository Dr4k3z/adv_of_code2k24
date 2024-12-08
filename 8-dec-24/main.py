import sys
sys.path.append('..')
from itertools import combinations
from utils import *

def find_nodes(data):
    res = []
    for i,row in enumerate(data):
        for j,cell in enumerate(row):
            if cell != '.':
                res.append((i,j,cell))
    return res

def part1():
    data = read_input('input.txt')
    data = [list(line) for line in data]

    M,N = len(data),len(data[0])

    nodes = find_nodes(data)
    antinodes = set()
    for (x1,y1,freq1),(x2,y2,freq2) in combinations(nodes,2):
        # same frequency
        if freq1 != freq2:
            continue

        dx,dy = x2-x1,y2-y1

        ant_1 = (x1-dx,y1-dy)
        ant_2 = (x2+dx,y2+dy)

        if ant_1[0] >= 0 and ant_1[1] >=0 and ant_1[0] < M and ant_1[1] < N:
            antinodes.add(ant_1)

        if ant_2[0] >= 0 and ant_2[1] >=0 and ant_2[0] < M and ant_2[1] < N:
            antinodes.add(ant_2)

    #print(f'Number of antinode: {len(antinodes)}')

def part2():
    data = read_input('input.txt')
    data = [list(line) for line in data]

    M,N = len(data),len(data[0])

    nodes = find_nodes(data)
    antinodes = set()
    for (x1,y1,freq1),(x2,y2,freq2) in combinations(nodes,2):
        # same frequency
        if freq2 != freq1:
            continue
        
        dx,dy = x2-x1,y2-y1
        for i in range(-M-N,M+N):
            new_x = x1 + i * dx
            new_y = y1 + i * dy

            if 0 <= new_x < M and 0 <= new_y < N:
                antinodes.add((new_x, new_y))   

    for x, y, _ in nodes:
        antinodes.add((x, y))

    #print(f'Number of antinode: {len(antinodes)}')

if __name__ == '__main__':
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    print(f'Part 1: {part1_time} ms')
    print(f'Part 2: {part2_time} ms')

    save_output(new_row=[part1_time, part2_time])
