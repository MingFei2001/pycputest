import multiprocessing
import time
import numpy as np


def cpu_intensive_task(index, start_time):
    while (time.perf_counter() - start_time) < 600:  # Run for 1 hour
        try:
            x = np.random.rand(10000000)
            y = np.sin(x)
            z = np.cos(y)
            w = np.tan(z)
        except Exception as e:
            print(f"Error in process {index}: {str(e)}")
        finally:
            # release any resources used by the process
            pass


def main():
    num_physical_cores = multiprocessing.cpu_count()
    print(f"Running on {
          num_physical_cores} physical core(s) and potentially more logical core(s).")

    start_time_all = time.perf_counter()

    processes = []
    for i in range(num_physical_cores):
        index = i
        p = multiprocessing.Process(
            target=cpu_intensive_task, args=(index, start_time_all))
        p.start()
        processes.append(p)

    while True:
        # do nothing, let the processes run indefinitely
        pass


if __name__ == "__main__":
    main()
