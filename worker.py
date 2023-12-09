import threading
from time import sleep
import mission

def worker(max_active_threads,process_id):
    max_active_threads += 1
    thread_id = 0
    while True:
        # Check the number of active threads
        active_threads = threading.active_count()

        for i in range(max_active_threads - active_threads):
            # Create a new thread
            new_thread = threading.Thread(target=mission.mission, args=(thread_id,process_id))
            new_thread.start()
            thread_id += 1

        if thread_id >= 100 :
            break

        sleep(0)

if __name__ == '__main__':
    print('worker.py')