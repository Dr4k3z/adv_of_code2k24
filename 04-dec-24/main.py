import sys
sys.path.append('..')
from utils import execution_time,save_output

alternatives = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,0),
    (1,-1),
    (1,1)
]

def look(i,j,mat, delta, wish):
    #print("look", i,j,delta, wish)
    if len(wish)==0:
        #print("true len")
        return True
    if i<0 or i>=len(mat):
        #print('i')
        return False
    if j<0 or j>=len(mat[i]):
        #print('j')
        return False
    if mat[i][j]!=wish[0]:
        #print('wish', wish, mat[i][j])
        return False
    return look(i+delta[0], j+delta[1], mat, delta, wish[1:])

def look2(i,j,mat,wish):
    #print("look", i,j,delta, wish)
    if len(wish)==0:
        #print("true len")
        return True
    if i<0 or i>=len(mat):
        #print('i')
        return False
    if j<0 or j>=len(mat[i]):
        #print('j')
        return False
    if mat[i][j]!=wish[0]:
        #print('wish', wish, mat[i][j])
        return False
    return True

def test(i,j,mat):
    count=0
    for d in alternatives:
        if look(i,j,mat,d, ['X','M','A','S']):
            count+=1
    return count

def diag(i,j,a,b,mat):
    return look2(i+a[0], j+a[1], mat, "M") and look2(i+b[0], j+b[1], mat, "S")

def test2(i,j,mat):
    if (diag(i,j,(-1,-1),(+1,+1), mat) or diag(i,j,(+1,+1),(-1,-1),mat)) and (diag(i,j,(-1,+1), (+1,-1), mat) or diag(i,j, (+1,-1), (-1,+1),mat)):
        return 1
    return 0

def part1():
    with open('input.txt') as file:
        mat = [l.strip() for l in file]

    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=='X':
                count+=test(i,j,mat)
    print(f'Number of XMAS = {count}')

def part2():
    with open('input.txt') as file:
        mat = [l.strip() for l in file]

    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=='A':
                count+=test2(i,j,mat)
    print(f'Number of X-MAS = {count}')
         
if __name__=="__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time, part2_time])