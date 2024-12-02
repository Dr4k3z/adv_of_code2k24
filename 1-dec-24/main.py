import heapq
from collections import Counter
import time

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
    with open('input.txt') as inputfile:
        data = inputfile.read().split('\n')

    data = [d.split() for d in data]

    list1 = [int(d) for d,_ in data]
    list2 = [int(d) for _,d in data]
    
    check_distance(list1, list2)
    

def part2():
    with open('input.txt') as inputfile:
        data = inputfile.read().split('\n')

    data = [d.split() for d in data]

    list1 = [int(d) for d,_ in data]
    list2 = [int(d) for _,d in data]
    
    similarity(list1,list2)
    

if __name__ == '__main__':
    p1_times = [0]*10
    for i in range(10):
        begin = time.time()
        part1()
        end = time.time()
        p1_times.append(end-begin)

    p2_times = [0]*10
    for i in range(10):
        begin = time.time()
        part2()
        end = time.time()
        p2_times.append(end-begin)

    print(f'Part One execution time: {sum(p1_times)/10}')
    print(f'Part Two execution time: {sum(p2_times)/10}')