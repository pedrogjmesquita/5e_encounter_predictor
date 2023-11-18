import threading

from MainThread import execute


for i in range(4):
    thread = threading.Thread(target=execute)
    thread.start()
    print(f'New thread started: {thread.name}')


