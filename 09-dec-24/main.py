import sys
sys.path.append('..')
from collections import Counter
from utils import read_input,execution_time,save_output

def part1():
    data = read_input('input.txt')
    data = data[0]

    file = []
    for i,el in enumerate(data):
        for _ in range(int(el)):
            if i % 2 == 0:
                file.append(str(i//2))
            else:
                file.append('.')

    n = Counter(file)['.']
    last_pos = len(file)-1

    for i in range(n):
        # swap first '.' with last number
        tmp = file[last_pos]
        point_idx = file.index('.')
        file[point_idx] = tmp
        file[last_pos] = '.'
        last_pos -= 1

        #print(''.join(file))

    #assert ''.join(file) == '0099811188827773336446555566..............', 'Test failed'
    #print('Test passed')
    total = sum([i*int(el) for i,el in enumerate(file[:last_pos+1])])
    #print(f'Filesystem checksum = {total}')

def part2():
    data = read_input('input.txt')
    data = [int(char) for char in data[0]]

    def sum_n(a, b):
        return (b-a+1)*(a+b)//2

    idxs = []
    b = 0
    for i in range(len(data)):
        idxs.append(b)
        b += data[i]

    res = 0
    id = len(data)//2
    for j in range(len(data)-1,-1,-2):
        fsize = data[j]
        for i in range(1, j, 2):
            if data[i] >= fsize:
                b = idxs[i]
                res += sum_n(b, b+fsize-1)*id
                idxs[i] += fsize
                data[i] -= fsize
                break
        else:
            b = idxs[j]
            res += sum_n(b, b+fsize-1)*id
        id -= 1

    #print(f'Filesystem checksum = {res}')    
    
if __name__ == '__main__':
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])