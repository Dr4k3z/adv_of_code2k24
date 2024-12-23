import sys
sys.path.append('..')
import time
from functools import lru_cache
from utils import read_input,save_output
from collections import defaultdict

@lru_cache(maxsize=None)
def toBinary(num : str) -> str:
    return bin(int(num))[2:]

@lru_cache(maxsize=None)
def mix(secret_num : str, num : str) -> None:
    M = max(len(secret_num), len(num))
    secret_num = secret_num.zfill(M)
    num = num.zfill(M)

    secret_num = ''.join('1' if a != b else '0' for a,b in zip(secret_num,num))
    return secret_num

@lru_cache(maxsize=None)
def prune(secret_num : str) -> None:
    # 16777216 = 2^24
    if len(secret_num) > 24:
        secret_num = secret_num[-24:]
    else:
        secret_num = secret_num
    
    return secret_num

@lru_cache(maxsize=None)
def multiply(num : str,power : int) -> str:
    return num+'0'*power

@lru_cache(maxsize=None)
def divide(num : str,power : int) -> str:
    if len(num) > power:
        return num[:-power]
    else:
        return '0'

def evolve(secret_num : str) -> str:
    # 64 = 2^6
    res = multiply(secret_num, 6)
    secret_num = mix(secret_num,res)
    secret_num = prune(secret_num)

    # 32 = 2^5
    res = divide(secret_num, 5)
    secret_num = mix(secret_num,res)
    secret_num = prune(secret_num)

    # 2048 = 2^11
    res = multiply(secret_num, 11)
    secret_num = mix(secret_num,res)
    secret_num = prune(secret_num)

    return secret_num

def part1():
    data = read_input('input.txt')
    total = 0 
    for i,num in enumerate(data):
        secret_num = toBinary(num)

        N = 2000
        for _ in range(N):
            secret_num = evolve(secret_num)

        #print(f'Done with {i+1}')

        total += int(secret_num,2)

    #print(f'Total = {total}')

def part2():
    # cant brute force part 2
    data = read_input('input.txt')
    prices_path = { i : [int(row[-1])] for i,row in enumerate(data)}

    for i in range(len(data)):
        secret_num = toBinary(data[i])

        N = 2000
        for _ in range(N):
            secret_num = evolve(secret_num)
            prices_path[i].append(int(str(int(secret_num,2))[-1]))

    #print('done with price history')

    diff = {i : [b-a for a,b in zip(prices_path[i],prices_path[i][1:])] for i in prices_path}
    sequence_results = defaultdict(lambda: defaultdict(int))
    for initial,changes in diff.items():
        sequences_seen = set() 
        for i in range(len(changes) - 4 + 1):
            current_sequence = tuple(changes[i:i + 4])
            if current_sequence not in sequences_seen:
                sequences_seen.add(current_sequence)
                resulting_price = prices_path[initial][i + 4]
                sequence_results[current_sequence][initial] = resulting_price
    
    best_sequence = None
    max_bananas = 0
    
    for sequence, results in sequence_results.items():
        total = sum(results[initial] for initial in prices_path.keys())
        if total > max_bananas:
            max_bananas = total
            best_sequence = sequence
    
    return list(best_sequence), max_bananas

if __name__ == '__main__':
    start = time.time()
    part1()
    part1_time = time.time() - start
    start = time.time()
    seq,gain = part2()
    part2_time = time.time() - start

    save_output(new_row=[part1_time,part2_time])