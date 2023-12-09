# Parallel Computing Demonstration with Python

This Python repository showcases parallel computing using the multiprocessing and threading libraries to achieve concurrent execution.

## Execution Details and Warnings

For ease of observation, task-related numbers will be displayed during execution, including the start of tasks and their respective completion times. Refer to the explanation in `mission.py` for details.

**Warning:** Excessive numbers of processes and threads may lead to 100% CPU usage, or even system crashes. Please consider the well-being of your computer XD.

## File Roles Overview

- **main.py:** Prompts the user for the desired number of processes and threads, then calls `manager.py`.
  
- **manager.py:** Establishes workers by calling `worker.py`, limits the number of workers based on the provided number of processes from `main.py`, and replenishes workers upon completion. The default is to end work after calling 100 workers. In this file, `process_id` corresponds to the worker.

- **worker.py:** Executes tasks by calling `mission.py`, limits the number of tasks based on the provided number of threads from `manager.py`, and replenishes tasks upon completion. The default is to end work after calling 100 tasks. In this file, `thread_id` corresponds to the mission.

- **mission.py:** The task to be executed. Here, a for loop is used for addition. When a mission starts, it prints out the `process_id` and `thread_id` (corresponding to worker and mission), and similarly when it ends, but with an additional display of execution time.
