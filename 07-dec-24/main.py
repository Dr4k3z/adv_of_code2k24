import sys
sys.path.append('..')
import itertools
import operator as op
from functools import reduce
from utils import read_input,execution_time,save_output
from math import prod

"""
    I shall learn better how to use itertools.product
    and reduce. The latter should be like eval, right?
"""

def check_res(res, nums):
    # base case
    if res == sum(nums):
        return True
    if res == prod(nums):
        return True
    
    for v in itertools.product([op.add, op.mul], repeat=len(nums)-1):
        if res == reduce(lambda x, v: v[0](x,v[1]), zip(v, nums[1:]), nums[0]):
            return True
    return False

def check_res_concat(res, nums):
    concat = lambda x,y : int(f'{x}{y}') # I know this shouldn't be here, but helps reading the code

    # base case
    if res == sum(nums):
        return True
    if res == prod(nums):
        return True
    
    for v in itertools.product([op.add, op.mul, concat], repeat=len(nums)-1):
        if res == reduce(lambda x, v: v[0](x,v[1]), zip(v, nums[1:]), nums[0]):
            return True
    return False

def part1(filename='input.txt'):
    data = read_input(filename)
    total = 0
    for line in data:
        result,nums = line.split(': ')
        nums = nums.split(' ')
        result = int(result)
        nums = list(map(int, nums))

        if check_res(result, nums):
            total += result

    #print(f'Counter: {total}')

def part2(filename='input.txt'):
    data = read_input(filename)
    total = 0
    for line in data:
        result,nums = line.split(': ')
        nums = nums.split(' ')
        result = int(result)
        nums = list(map(int, nums))

        if check_res_concat(result, nums):
            total += result

    #print(f'Counter: {total}')

if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])