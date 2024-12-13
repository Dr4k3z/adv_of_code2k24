import sys
sys.path.append('..')
from utils import read_input,save_output
import time

def print_region(region,letter):
    for i in range(M):
        for j in range(N):
            if (i,j) in region:
                print(letter,end='')
            else:
                print('.',end='')
        print()
    
def is_contiguous(regions,q):
    for reg in regions:
        for p in reg:
            if abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1:
                return reg
    return None

data = read_input('input.txt')
plants = set(''.join(data))

M, N = len(data), len(data[0])

# this code is shite
def find_regions(plant):
    def add_to_region(regions, point):
        for reg in regions:
            if any(abs(p[0] - point[0]) + abs(p[1] - point[1]) == 1 for p in reg):
                reg.append(point)
                return True
        return False

    regions = []
    for i in range(M):
        for j in range(N):
            if data[i][j] == plant:
                if not add_to_region(regions, (i, j)):
                    regions.append([(i, j)])

    merged = True
    while merged:
        merged = False
        for i in range(len(regions)):
            for j in range(i + 1, len(regions)):
                if any(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) == 1 for p1 in regions[i] for p2 in regions[j]):
                    regions[i].extend(regions[j])
                    del regions[j]
                    merged = True
                    break
            if merged:
                break
    return regions


def perimiter(coordinates):
    garden_set = set(coordinates) 
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in coordinates:
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in garden_set:
                perimeter += 1

    return perimeter

def part1():
    regions = {}
    for plant in plants:
        regions[plant] = find_regions(plant)

    total = 0
    for key,val in regions.items():
        for reg in val:
            per = perimiter(reg)
            area = len(reg)
            total += area*per
            #print(f'{key} area = {area}  per = {per} total = {area*per}')

    print(f'Total fence: {total}')

if __name__ == "__main__":
    start = time.time()
    part1()
    end = time.time()

    part1_time = end - start
    save_output(new_row=[part1_time,'N/A'])