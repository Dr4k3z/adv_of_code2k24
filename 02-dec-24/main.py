import sys
sys.path.append('..')
from utils import execution_time,save_output

def stable(level) -> bool:
    if not( level == sorted(level) or level == sorted(level, reverse=True) ):
        return False
    
    diffs = [abs(level[i]-level[i-1]) for i in range(1, len(level))]

    if max(diffs) <= 3 and min(diffs) >= 1:
        return True
    return False

def stable_dampener(levels) -> bool:
    if stable(levels):
        return True

    for i in range(len(levels)):
        if stable(levels[:i] + levels[i+1:]):
            return True
    return False

def part1():
    """
        Avg execution time: 2*10^-3 s
    """
    with open('input.txt') as inputfile:
        reports = inputfile.read().splitlines()

    count = 0
    for report in reports:
        levels = report.split(' ')
        levels = [int(el) for el in levels]
        
        if stable(levels):
            count += 1

    #print(f'Number of stable levels = {count}')

def part2():
    """
        Avg execution time: 5*10^-3 s
    """
    with open('input.txt') as inputfile:
        reports = inputfile.read().splitlines()

    count = 0
    for report in reports:
        levels = report.split(' ')
        levels = [int(el) for el in levels]
        
        if stable_dampener(levels):
            count += 1

    #print(f'Number of stable levels = {count}')

if __name__ == '__main__':
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)
    print(f'Part One execution time: {part1_time}')
    print(f'Part One execution time: {part2_time}')
    save_output(new_row=[part1_time, part2_time])