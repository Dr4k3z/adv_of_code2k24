import sys
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt
from utils import read_input,execution_time,save_output
from math import prod
from collections import Counter
from scipy.stats import kstest

class Robot:
    def __init__(self,pos,vel):
        self.pos = pos
        self.vel = vel

    def __str__(self):
        return f'pos=<x={self.pos[0]}, y={self.pos[1]}>, vel=<x={self.vel[0]}, y={self.vel[1]}>'

M,N = 103,101

def print_map(robots):
    pos_counter = Counter([robot.pos for robot in robots])

    for i in range(M):
        for j in range(N):
            if (j,i) in pos_counter.keys():
                print(pos_counter[(j,i)], end='')
            else:
                print('.', end='')
        print()

def move(robot):
    new_pos = ((robot.pos[0] + robot.vel[0]) % N, (robot.pos[1] + robot.vel[1]) % M)
    return Robot(new_pos, robot.vel)

def picture(robots):
    pos_counter = Counter([robot.pos for robot in robots])

    picture = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            picture[i,j] = pos_counter[(j,i)]
    return picture

def compute_safety_factor(robots):
    first_quad = [robot for robot in robots if robot.pos[0] < N//2 and robot.pos[1] < M//2]
    second_quad = [robot for robot in robots if robot.pos[0] > N//2 and robot.pos[1] < M//2]
    third_quad = [robot for robot in robots if robot.pos[0] < N//2 and robot.pos[1] > M//2]
    fourth_quad = [robot for robot in robots if robot.pos[0] > N//2 and robot.pos[1] > M//2]

    # lmao
    safety_factor = prod(list(map(len, [first_quad, second_quad, third_quad, fourth_quad])))
    return safety_factor

def part1():
    data = read_input('input.txt')
    robots = []
    for robot in data:
        pos_str, vel_str = robot.split(' ')
        pos = tuple(map(int, pos_str[2:].split(',')))
        vel = tuple(map(int, vel_str[2:].split(',')))
        robots.append(Robot(pos, vel))

    for _ in range(100):
        robots = [move(robot) for robot in robots]
    
    print(f'Safety factor: {compute_safety_factor(robots)}')

def part2():
    data = read_input('input.txt')

    robots = []
    for robot in data:
        pos_str, vel_str = robot.split(' ')
        pos = tuple(map(int, pos_str[2:].split(',')))
        vel = tuple(map(int, vel_str[2:].split(',')))
        robots.append(Robot(pos, vel))

    factors = []
    for _ in range(M*N):
        robots = [move(robot) for robot in robots]

        #print_map(robots)
        #print('--------')
        factors.append(compute_safety_factor(robots))

        x_pos = [robot.pos[0] for robot in robots]
        y_pos = [robot.pos[1] for robot in robots]
        stat_x,pval_x = kstest(x_pos, 'uniform', args=(0,N))
        stat_y,pval_y = kstest(y_pos, 'uniform', args=(0,M))

        if (pval_x < 0.01) and (pval_y < 0.01):
            print(f'Suspicious configuration! Iteration: {_}')
            pic = picture(robots)
            plt.matshow(pic)
            plt.title(f'Iteration {_}')
            plt.show()

if __name__ == '__main__':
    part1_time = execution_time(part1)

    save_output(new_row=[part1_time,'Not measured'])