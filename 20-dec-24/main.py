import sys
sys.path.append('..')
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from utils import read_input,execution_time,save_output
from collections import defaultdict,deque

def print_map(data):
    for row in data:
        print(row)

data = read_input('input.txt')

M, N = len(data), len(data[0])
start = end = None

for i in range(M):
    for j in range(N):
        if data[i][j] == 'S':
            start = (i, j)
        elif data[i][j] == 'E':
            end = (i, j)

# find shortest path
def is_valid(data, i, j, seen):
    if 0 <= i < M and 0 <= j < N and data[i][j] != '#' and (i, j) not in seen:
        return True
    return False

def bfs():
    q = deque([(start[0],start[1],[start])])
    seen = set()
    seen.add(start)
    while q:
        i, j, path = q.popleft()
        if (i, j) == end:
            return path
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if is_valid(data, ni, nj, seen):
                seen.add((ni, nj))
                q.append((ni, nj, path + [(ni, nj)]))

'''
def visualize(data, path):
    # build graph
    G = nx.Graph()
    for j in range(M):
        for i in range(N):
            if data[i][j] != '#':
                G.add_node((i, j))
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if is_valid(data, ni, nj, set()):
                        G.add_edge((i, j), (ni, nj))

    # draw graph
    def plot_graph(G, path = None):
        pos = {node: (node[0], -node[1]) for node in G.nodes()}
        nx.draw(G, pos, with_labels=True, node_size=20, node_color='lightblue', font_size=1, font_weight='bold')

        if path:
            edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=5)

        plt.show()

    plot_graph(G, path)
'''

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1(num_cheat = 2):
    init_path = bfs()
    path_length = len(init_path) - 1

    cost_start = {p : i for i,p in enumerate(init_path)}
    cost_end = {p : i for i,p in enumerate(reversed(init_path))}

    savings = defaultdict(int)
    counter = 0
    for u,v in combinations(init_path, 2):
        dist = manhattan_dist(u, v)
        if dist > num_cheat:
            continue

        saved_cost = path_length - (cost_start[u] + cost_end[v]+dist)
        savings[saved_cost] += 1
        if saved_cost >= 100:
            counter += 1

    #print(savings)
    #print(f'Number of path with savings >= 100: {counter}')

def part2():
    num_cheat = 20
    part1(num_cheat)

if __name__ == '__main__':
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])