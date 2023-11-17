import threading

from MainThread import execute

for _ in range(8):
    thread = threading.Thread(target=execute)
    thread.start()
    print(f'New thread started: {thread.name}')

