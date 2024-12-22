import os
import time
import networkx as nx
import matplotlib.pyplot as plt

def execution_time(func, n_samples : int = 10):
    times = [0]*n_samples

    for i in range(n_samples):
        begin = time.time()
        func()
        end = time.time()
        times[i] = end-begin

    return sum(times)/n_samples

def read_input(filename='input.txt', to_int=False):
    lines = []
    with open(filename) as file:
        for line in file:
            if to_int:
                stripped = line.strip()
                stripped = [int(c) for c in stripped]
                lines.append(stripped)
            else:
                lines.append(line.strip())
    return lines

def save_output(file_path='../README.md', new_row=[0.0,0.0]):
    current_dir = os.getcwd()
    dir_name = os.path.basename(current_dir)

    new_row = list(map(str, new_row))
    new_row.insert(0, dir_name)    

    with open(file_path, "r") as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        if line.startswith("|") and not line.strip().startswith("|---"):
            lines.insert(i + 2, "| " + " | ".join(new_row) + " |\n")
            break

    with open(file_path, "w") as file:
        file.writelines(lines)

def plot_graph(G, path = None):
    pos = {node: (node[0], -node[1]) for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, node_size=20, node_color='lightblue', font_size=1, font_weight='bold')

    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=5)

    plt.show()