import sys
sys.path.append('..')
from utils import read_input,execution_time,save_output

def is_possible(pattern, towels):
    n = len(pattern)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for towel in towels:
            if i >= len(towel):
                if pattern[i-len(towel):i] == towel and dp[i-len(towel)]:
                    dp[i] = True
                    break

    return dp[n]


def decomp(target, substrings):
    n = len(target)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for substring in substrings:
            substr_len = len(substring)
            if (i >= substr_len and 
                target[i-substr_len:i] == substring):
                dp[i] += dp[i-substr_len]
    
    return dp[n]
         

def part1():
    data = read_input('input.txt')

    towels = [towel.strip() for towel in data[0].split(',')]
    patterns = data[2:]

    total_patterns = 0    
    for i,pattern in enumerate(patterns):
        if is_possible(pattern, towels):
            total_patterns += 1

    #print(f'Total patterns: {total_patterns}')

def part2():
    data = read_input('input.txt')

    towels = [towel.strip() for towel in data[0].split(',')]
    patterns = data[2:]

    total_decomp = 0    
    for i,pattern in enumerate(patterns):
        if is_possible(pattern, towels):
            total_decomp += decomp(pattern, towels)

    #print(f'Total decompositions: {total_decomp}')

if __name__ == '__main__':
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time, part2_time])