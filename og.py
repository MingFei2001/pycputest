# AI code
import multiprocessing
import time
import numpy as np


def cpu_intensive_task(index):
    start_time = time.perf_counter()
    while (time.perf_counter() - start_time) < 600:
        x = np.random.rand(10000000)
        y = np.sin(x)
        z = np.cos(y)
        w = np.tan(z)


def main():
    num_physical_cores = multiprocessing.cpu_count()
    print(f"Running on {
          num_physical_cores} physical core(s) and potentially more logical core(s).")

    processes = []
    start_time_all = time.perf_counter()
    for i in range(num_physical_cores):
        index = i
        p = multiprocessing.Process(target=cpu_intensive_task, args=(index,))
        p.start()
        processes.append(p)

    while True:
        # do nothing, let the processes run indefinitely
        pass


if __name__ == "__main__":
    main()
