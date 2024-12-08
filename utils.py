import os
import time

def execution_time(func, n_samples : int = 10):
    times = [0]*n_samples

    for i in range(n_samples):
        begin = time.time()
        func()
        end = time.time()
        times[i] = end-begin

    return sum(times)/n_samples

def read_input(filename='input.txt'):
    lines = []
    with open(filename) as file:
        for line in file:
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
