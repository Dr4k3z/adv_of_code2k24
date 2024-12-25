import sys
sys.path.append('..')
import numpy as np
from utils import execution_time,save_output

def parse_file(filename):
    with open(filename, 'r') as file:
        raw_data = file.read()

    block_strings = raw_data.strip().split('\n\n')

    def convert_to_np_array(block):
        return np.array([list(line) for line in block.split('\n')])

    blocks = [convert_to_np_array(block) for block in block_strings]
    return blocks

def part1():
    parsed_data = parse_file('input.txt')

    locks,keys = [],[]
    for chunk in parsed_data:
        if chunk[0][0] == '#':
            locks.append(chunk)
        else:
            keys.append(chunk)

    def decode_locks(lock, seq=False):
        _,N = len(lock),len(lock[0])
        nums = []

        lock = lock.T
        for col in range(N):
            idx = np.where(lock[col] == '#')[0][-1]
            nums.append(idx)
        return nums

    def decode_keys(key, seq=True):
        M,N = len(key),len(key[0])
        nums = []

        key = key.T
        for col in range(N):
            idx = M-np.where(key[col] == '#')[0][0]-1
            nums.append(idx)
        return nums

    def overlap(lock,key):
        N = len(lock)
        for i in range(N):
            if lock[i] + key[i] > N:
                return True
        return False

    locks = [decode_locks(lock,seq=False) for lock in locks]
    keys = [decode_keys(key,seq=True) for key in keys]

    fits = set()
    for lock in locks:
        for key in keys:
            if not overlap(lock,key):
                fits.add((tuple(lock),tuple(key)))

    #print(len(fits))

if __name__=="__main__":
    part1_time = execution_time(part1)
    save_output(new_row=[part1_time,'**'])