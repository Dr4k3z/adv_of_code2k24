import sys
sys.path.append('..')
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from utils import read_input,execution_time,save_output

def plot_graph(G, path = None):
    pos = {node: (node[1], -node[0]) for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, node_size=10, node_color='lightblue', font_size=1, font_weight='bold')

    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=5)

    plt.show()                    

def custom_dijkstra(graph, start, end, init_dir):
    pq = []
    heapq.heappush(pq, (0, start, init_dir, [start]))

    visited = {}
    while pq:
        curr_cost, curr_node, curr_dir, path = heapq.heappop(pq)

        if curr_node == end:
            return curr_cost, path

        if (curr_node, curr_dir) in visited and visited[(curr_node, curr_dir)] <= curr_cost:
            continue

        visited[(curr_node, curr_dir)] = curr_cost

        for neighbor in graph.neighbors(curr_node):
            new_dir = (neighbor[0] - curr_node[0], neighbor[1] - curr_node[1])
            edge_cost = 1 if new_dir == curr_dir else 1001

            heapq.heappush(pq, (curr_cost + edge_cost, neighbor, new_dir, path + [neighbor]))

    return float('inf'), []

def find_all_best_paths(graph, start, end, init_dir):
    pq = [(0, start, init_dir)]  
    costs = {start: 0}
    predecessors = {start: []}

    while pq:
        cost, node, curr_dir = heapq.heappop(pq)

        if cost > costs.get(node, float('inf')):
            continue

        for neighbor in graph.neighbors(node):
            new_dir = (neighbor[0] - node[0], neighbor[1] - node[1])
            edge_cost = 1 if new_dir == curr_dir else 1001
            new_cost = cost + edge_cost

            if new_cost < costs.get(neighbor, float('inf')):
                costs[neighbor] = new_cost
                predecessors[neighbor] = [node]
                heapq.heappush(pq, (new_cost, neighbor, new_dir))
            elif new_cost == costs.get(neighbor, float('inf')):
                predecessors[neighbor].append(node)

    best_path_nodes = set()

    def backtrack(node):
        if node in best_path_nodes:
            return
        best_path_nodes.add(node)
        for pred in predecessors.get(node, []):
            backtrack(pred)

    backtrack(end)

    return best_path_nodes

def part1():
    data = read_input('example.txt')

    M,N = len(data),len(data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    G = nx.DiGraph()

    for r in range(M):
        for c in range(N):
            if data[r][c] in {'.', 'S', 'E'}:
                G.add_node((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and data[nr][nc] in {'.', 'S', 'E'}:
                        G.add_edge((r, c), (nr, nc))

    start = ()
    end = ()
    for i,row in enumerate(data):
        for j,cell in enumerate(row):
            if cell == 'S':
                start = (i,j)
            if cell == 'E':
                end = (i,j)
            
        if start and end:
            break

    init_dir = (0, 1)
    min_cost, optimal_path = custom_dijkstra(G, start, end, init_dir)
    print("Minimum cost:", min_cost)
    #plot_graph(G, optimal_path)

def part2():
    data = read_input('input.txt')

    M,N = len(data),len(data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    G = nx.DiGraph()

    for r in range(M):
        for c in range(N):
            if data[r][c] in {'.', 'S', 'E'}:
                G.add_node((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and data[nr][nc] in {'.', 'S', 'E'}:
                        G.add_edge((r, c), (nr, nc))

    start = ()
    end = ()
    for i,row in enumerate(data):
        for j,cell in enumerate(row):
            if cell == 'S':
                start = (i,j)
            if cell == 'E':
                end = (i,j)
            
        if start and end:
            break

    init_dir = (0, 1)
    best_paths = find_all_best_paths(G, start, end, init_dir)

    counter = 0
    for r in range(M):
        row = []
        for c in range(N):
            if (r, c) in best_paths:
                counter += 1

    print(f'Number of tiles: {counter}')

if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time,part2_time])