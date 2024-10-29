# PycpuTest
![Pycputest Logo](https://img.shield.io/badge/Languages-Python%20(3.8+)%20-%2300A86FC)

## Overview
PycpuTest is a Python script designed to stress the CPU's capabilities by performing computationally intensive tasks for a specified time period. This project utilizes multiple processes to take full advantage of multiple-core CPUs.

## Features
- CPU Stressing: PycpuTest generates random numbers, calculates their sine, cosine, and tangent values, and stores these calculations in memory for an extended period.
- Multithreading/Multiprocessing: The script utilizes Python's multiprocessing module to spawn multiple processes that execute the same task concurrently.

## Installation
1. Clone this repository using your preferred method (e.g., Git CLI or GitHub Desktop).
2. Open a terminal or command prompt and navigate to the project directory.
3. Install dependencies by running pip install -r requirements.txt.
4. Run the script by typing python main.py (replace main.py with your actual Python file name).

## Usage
To use PycpuTest:

1. Modify the time_period variable in the main.py file to change the duration of the CPU stressing process.
2. Execute the script using python main.py.
3. Monitor the CPU utilization and system resources during execution.
