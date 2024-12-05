import sys
sys.path.append('..')
from utils import execution_time, read_input
from collections import defaultdict
from functools import cmp_to_key

def check_order(line, rules):
    for el in line:
        rule = rules[el]
        for val in rule:
            if val in line:
                val_idx = line.index(val)
                el_idx = line.index(el)

                if val_idx < el_idx:
                    return False
    
    return True

def get_comparator(lookup):
    def compare_by_precedence(a, b):
        if b in lookup[a]:
            return -1
        return 1 if a in lookup[b] else 0

    return compare_by_precedence

def part1():
    rules_data = read_input('example_rules.txt')

    rules = defaultdict(set)
    for line in rules_data:
        key, value = line.split('|')
        rules[int(key)].add(int(value))

    update_data = read_input('example.txt')
    update_data = [list(map(int, line.split(','))) for line in update_data]

    total = 0
    for update in update_data:
        if check_order(update, rules):
            total += update[len(update)//2]
    
    #print(f'Sum of correct lines: {total}')

def part2():
    rules_data = read_input('rules.txt')

    rules = defaultdict(set)
    for line in rules_data:
        key, value = line.split('|')
        rules[int(key)].add(int(value))

    update_data = read_input('input.txt')
    update_data = [list(map(int, line.split(','))) for line in update_data]

    total = 0
    for update in update_data:
        if not check_order(update, rules):
            sorted_update = sorted(update, key=cmp_to_key(get_comparator(rules)))
            n = len(sorted_update)
            total += sorted_update[n//2]

    #print(f'Sum of not-correct lines: {total}')

if __name__ == '__main__':
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)
    print(f'Part One execution time: {part1_time}')
    print(f'Part One execution time: {part2_time}')