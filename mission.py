from time import process_time

def mission(thread_id,process_id):
    time_start = process_time()
    print(f"Process {process_id} Thread {thread_id}: Started.")

    num = thread_id + process_id
    for i in range(10000000):
        num += i

    time_end = process_time()
    print(f"Process {process_id} Thread {thread_id}: Finished. Took {time_end - time_start} seconds.")

    return num

if __name__ == '__main__':
    print('mission.py')