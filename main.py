import manager

if __name__ == "__main__":
    print("max_active_processes:", end=" ")
    max_active_processes = int(input())
    print("max_active_threads:", end=" ")
    max_active_threads = int(input())
    manager.manager(max_active_processes,max_active_threads)