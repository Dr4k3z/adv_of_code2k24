import sys
sys.path.append('..')
from math import log2
from functools import lru_cache
from utils import read_input

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
    data = read_input('example.txt')
    total = 0 
    for i,num in enumerate(data):
        secret_num = toBinary(num)

        N = 2000
        for _ in range(N):
            secret_num = evolve(secret_num)

        print(f'Done with {i+1}')

        total += int(secret_num,2)

    print(f'Total = {total}')

def part2():
    data = read_input('example2.txt')
    #prices = { i : [int(row[-1])] for i,row in enumerate(data)}

    secret_num = toBinary(data[0])
    prices = [int(data[0][-1])]
    N = 2000
    for _ in range(N):
        secret_num = evolve(secret_num)
        prices.append(int(str(int(secret_num,2))[-1]))

    diff = [b-a for a,b in zip(prices,prices[1:])]
    
    while prices:
        M = max(prices)
        M_idx = prices.index(M)

        if M_idx >= 4:
            print(f'{M} - {diff[M_idx-3:M_idx+1]}')
            break
        else:
            prices.remove(M)



if __name__ == '__main__':
    #part1()
    part2()