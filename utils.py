import time

def execution_time(func, n_samples : int = 10):
    times = [0]*n_samples

    for i in range(n_samples):
        begin = time.time()
        func()
        end = time.time()
        times[i] = end-begin

    return sum(times)/n_samples