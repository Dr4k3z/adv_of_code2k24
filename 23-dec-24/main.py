import sys
sys.path.append('..')
import networkx as nx
import matplotlib.pyplot as plt
from utils import read_input,execution_time,save_output

def part1():
    data = read_input('input.txt')

    G = nx.Graph()

    computers = set()
    for line in data:
        a,b = line.split('-')

        if a not in computers:
            G.add_node(a)
            computers.add(a)
        if b not in computers:
            G.add_node(b)
            computers.add(b)

        G.add_edge(a,b)

    def contains_t(nodes):
        return any(node.startswith('t') for node in nodes)

    counter = 0
    for clicque in nx.enumerate_all_cliques(G):
        if len(clicque) == 3 and contains_t(clicque):
            counter += 1

    print(f'Number of cliques: {counter}')

def part2():
    data = read_input('input.txt')

    G = nx.Graph()

    computers = set()
    for line in data:
        a,b = line.split('-')

        if a not in computers:
            G.add_node(a)
            computers.add(a)
        if b not in computers:
            G.add_node(b)
            computers.add(b)

        G.add_edge(a,b)

    max_clique = max(nx.find_cliques(G), key=len)
    print(','.join(sorted(list(max_clique))))

if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])

    #nx.draw(G, with_labels=True)
    #plt.show()