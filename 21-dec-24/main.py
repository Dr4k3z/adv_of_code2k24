import sys
sys.path.append('..')
from utils import read_input

data = read_input('example.txt')

display = [
    (7,8,9),
    (4,5,6),
    (1,2,3),
    (None,0,'A')
]

start = (3,2)
target = data[0]

for c in target:
    pass