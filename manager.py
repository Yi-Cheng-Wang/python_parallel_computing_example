import multiprocessing
from time import sleep
import worker

def manager(max_active_processes, max_active_threads):
    process_id = 0
    while True:
        # Check the number of active processes
        active_processes = len(multiprocessing.active_children())

        for i in range(max_active_processes - active_processes):
            # Create a new process
            new_process = multiprocessing.Process(target=worker.worker, args=(max_active_threads,process_id))
            new_process.start()
            process_id += 1
        
        if process_id >= 100 :
            break

        sleep(0)

if __name__ == "__main__":
    print("manager.py")