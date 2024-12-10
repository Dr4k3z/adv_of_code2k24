import sys
sys.path.append('..')
import networkx as nx
from itertools import product
from collections import defaultdict
from utils import read_input,execution_time,save_output

def build_graph():
    data = read_input('input.txt', to_int=True)
    data = [list(row) for row in data]

    # find the roots
    roots = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                roots.append((i, j))

    # find the nines
    nines = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 9:
                nines.append((i, j))

    # build graph
    M,N = len(data),len(data[0])
    G = nx.DiGraph()

    for i in range(M):
        for j in range(N):
            G.add_node((i,j))
            if i > 0 and data[i][j] - data[i-1][j] == 1:
                G.add_edge((i-1, j), (i, j))
            if i < M - 1 and data[i][j] - data[i+1][j] == 1:
                G.add_edge((i+1, j), (i, j))
            if j > 0 and data[i][j] - data[i][j-1] == 1:
                G.add_edge((i, j-1), (i, j))
            if j < N - 1 and data[i][j] - data[i][j+1] == 1:
                G.add_edge((i, j+1), (i, j))

    #nx.draw(G, with_labels=True, font_weight='bold')
    #plt.show()
    return G,roots,nines

#paths = defaultdict(int)
def part1():
    G,roots,nines = build_graph()

    total_paths = 0
    for zero,nine in product(roots,nines):
        if nx.has_path(G, zero, nine):
            total_paths += 1
            #print(f'Path from {zero} to {nine}: {nx.has_path(G, zero, nine)}')

    #print(f'Number of paths: {total_paths}')

def part2():
    G,roots,nines = build_graph()   

    ratings = defaultdict(int)
    for zero,nine in product(roots,nines):
        paths = nx.all_simple_paths(G, zero, nine)
        #print(f'Number of paths from {zero} to {nine}: {len(list(paths))}')
        ratings[zero] += len(list(paths))
    #print(f'Total rating = {sum(ratings.values())}')

if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    print(f'Part 1: {part1_time} s')
    print(f'Part 2: {part2_time} s')

    save_output(new_row=[part1_time,part2_time])