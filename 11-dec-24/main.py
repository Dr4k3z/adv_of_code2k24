import sys
sys.path.append('..')
import time
from utils import read_input,save_output
from typing import Union
from collections import Counter,defaultdict

data = read_input('input.txt')[0]
data = tuple(map(int, data.split()))

def rules(num: int) -> Union[tuple,int]:
    if num == 0:
        return [1]
    
    num_str = str(num)
    N = len(num_str)
    if N % 2 == 0:
        middle_idx = N // 2
        return map(int, (num_str[:middle_idx], num_str[middle_idx:]))
    return [num * 2024]

def update(data, k=3):
    stones = Counter(int(num) for num in data)

    for _ in range(k):
        new_stones = defaultdict(int)
        for stone,count in stones.items():
            for q in rules(stone):
                new_stones[q] += count
        stones = new_stones

    return stones

if __name__ == "__main__":
    begin = time.time()
    stones = update(data,25)
    end = time.time()
    part1_time = end-begin

    begin = time.time()
    stones = update(data,75)
    end = time.time()
    part2_time = end-begin

    save_output(new_row=[part1_time,part2_time])
    #print(f'Number of stones after {25} blinks: {sum(stones.values())}')

    #stones = update(data,75)
    #print(f'Number of stones after {75} blinks: {sum(stones.values())}')
    