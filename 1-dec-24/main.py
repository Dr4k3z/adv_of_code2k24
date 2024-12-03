import sys
sys.path.append('..')

import heapq
from collections import Counter
from utils import execution_time

def check_distance(list1,list2):
    heapq.heapify(list1)
    heapq.heapify(list2)

    total_dist = 0
    while list1:
        left = heapq.heappop(list1)
        right = heapq.heappop(list2)
        total_dist += abs(left-right)

    return total_dist

def similarity(list1,list2):
    score = 0
    counter = Counter(list2)
    for el in list1:
        score += el*counter[el]
    return score


def part1():
    """
        Avg execution time: 10^-3 s
    """
    with open('input.txt') as inputfile:
        data = inputfile.read().split('\n')

    data = [d.split() for d in data]

    list1 = [int(d) for d,_ in data]
    list2 = [int(d) for _,d in data]
    
    check_distance(list1, list2)
    

def part2():
    """
        Avg execution time: 10^-3 s
    """
    with open('input.txt') as inputfile:
        data = inputfile.read().split('\n')

    data = [d.split() for d in data]

    list1 = [int(d) for d,_ in data]
    list2 = [int(d) for _,d in data]
    
    similarity(list1,list2)
    

if __name__ == '__main__':
    print(f'Part One execution time: {execution_time(part1)}')
    print(f'Part Two execution time: {execution_time(part2)}')