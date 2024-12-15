import sys
sys.path.append('..')
import copy
from collections import Counter
from utils import read_input,execution_time,save_output

def print_map(map):
    for row in map:
        print(''.join(row))

def starting_point(map):
    starting_pos = []
    starting_dir = []

    for i,row in enumerate(map):
        for j,el in enumerate(row):
            if el == '>':
                starting_pos = [i,j]
                starting_dir = [0,1]
            elif el == '<':
                starting_pos = [i,j]
                starting_dir = [0,-1]
            elif el == '^':
                starting_pos = [i,j]
                starting_dir = [-1,0]
            elif el == 'v':
                starting_pos = [i,j]
                starting_dir = [1,0]

    return starting_pos,starting_dir    

def move(pos, dir, map):
        N = len(map)
        M = len(map[0])

        new_pos = [pos[0]+dir[0], pos[1]+dir[1]]

        if new_pos[0] >= N or new_pos[1] >= M or new_pos[0] < 0 or new_pos[1] < 0:
            #print('Out of the map')
            return None
        if map[new_pos[0]][new_pos[1]] == '#' or map[new_pos[0]][new_pos[1]] == 'O':
            #print('Change of dir')
            dir = [dir[1], -dir[0]]
            return pos,dir
        if map[new_pos[0]][new_pos[1]] in ['.','X']:
            #map[pos[0]][pos[1]] = 'X'
            return new_pos,dir

def part1():
    map = read_input('input.txt')
    map = [list(row) for row in map]

    starting_pos, starting_dir = starting_point(map)    

    while move(starting_pos, starting_dir, map):
        starting_pos, starting_dir = move(starting_pos, starting_dir, map)

    map = ''.join([str(row) for row in map])
    print(Counter(map)['X']+1)

def check_cicle(map, starting_pos, starting_dir):
    already_visited = []

    while move(starting_pos, starting_dir, map):
        starting_pos, starting_dir = move(starting_pos, starting_dir, map)
        if (starting_pos,starting_dir) in already_visited:
            return True
        
        #print_map(map)
        #print('--------------')

        already_visited.append((starting_pos,starting_dir))
    return False

def part2():
    map = read_input('input.txt')
    map = [list(row) for row in map]

    map_cp = [copy.deepcopy(row) for row in map]

    starting_pos, starting_dir = starting_point(map)
    standard_path = [starting_pos]
    while move(starting_pos, starting_dir, map):
        p, d = move(starting_pos, starting_dir, map)
        
        if p != starting_pos:
            standard_path.append(p)
        
        starting_pos, starting_dir = p,d
        
    map = read_input('input.txt')
    map = [list(row) for row in map]

    starting_pos, starting_dir = starting_point(map) # needed repetitio
    k = 0
    for el in standard_path:
        new_map = [copy.deepcopy(row) for row in map_cp]

        new_map[el[0]][el[1]] = 'O'
        if check_cicle(new_map, starting_pos, starting_dir):
            #print_map(new_map)
            #print('-----------------')
            k += 1
            print(k)

if __name__ == '__main__':
    part1_time = execution_time(part1)
    print(f"Execution time: {part1_time}")

    #part2()

    save_output(new_row=[part1_time, 'N/A'])