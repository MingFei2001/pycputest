import multiprocessing
import time
import numpy as np


def cpu_intensive_task(index, start_time):
    print(f"Process {index} started.")
    while (time.perf_counter() - start_time) < 60:  # Run for 1 minute
        try:
            x = np.random.rand(10000000)
            y = np.sin(x)
            z = np.cos(y)
            w = np.tan(z)
            print(x + y + z + w)
        except Exception as e:
            print(f"Error in process {index}: {str(e)}")
        finally:
            # release any resources used by the process
            print("Process ended.")
            pass


def main():
    num_physical_cores = multiprocessing.cpu_count()
    print("CPU Stressing Tool started. Press Ctrl+C to stop.")
    print(f"Running on {
          num_physical_cores} physical cores and potentially more logical cores.")

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
