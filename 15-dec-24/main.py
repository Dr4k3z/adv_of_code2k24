import sys
sys.path.append('..')
from utils import read_input,execution_time,save_output

def print_map(m):
    for row in m:
        print(''.join(row))

def move(map, robot_pos, direction):
    move=False

    nx = robot_pos[0]+direction[0]
    ny = robot_pos[1]+direction[1]

    bx = nx
    by = ny
    box = False

    while map[bx][by] == 'O':
        box=True
        bx = bx+direction[0]
        by = by+direction[1]
    if box and map[bx][by]=='.':
        map[bx][by]='O'
        move = True
    if map[nx][ny]=='.':
        move=True
    
    if move:
        map[robot_pos[0]][robot_pos[1]] = '.'
        map[nx][ny]='@'
        return (nx,ny)
    
    return robot_pos

def gps(map,box):
    if map[box[0]][box[1]] != 'O':
        raise RuntimeError('Box not found')
    return 100*box[0]+box[1]

def part1():
    data = read_input('input.txt')
    init_map, instructions = [], []
    flag = True

    for line in data:
        if not line:
            flag = False
            continue
        (init_map if flag else instructions).append(list(line) if flag else line)

    instructions = ''.join(instructions)

    directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    robot_pos = (0,0)
    for i, row in enumerate(init_map):
        for j, cell in enumerate(row):
            if cell == '@':
                robot_pos = (i, j)
                break

    for inst in instructions:
        robot_pos = move(init_map,robot_pos,directions[inst])

    boxes = [(i,j) for i in range(len(init_map)) for j in range(len(init_map[i])) if init_map[i][j] == 'O']
    print(f'GPS Score: {sum(map(lambda x: gps(init_map,x),boxes))}')

def part2():
    data = read_input('input.txt')
    init_map, instructions = [], []
    flag = True

    for line in data:
        if not line:
            flag = False
            continue
        (init_map if flag else instructions).append(list(line) if flag else line)

    instructions = ''.join(instructions)

    directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    ### TODO

if __name__ == '__main__':
    part1_time = execution_time(part1)

    save_output(new_row=[part1_time,'N/A'])