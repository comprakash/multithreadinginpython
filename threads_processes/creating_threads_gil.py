import time
from threading import Thread


def do_work():
    print("Starting work")
    i = 0
    for _ in range(200000000):
        i += 1
    print("Finished work")


for _ in range(12):
    t = Thread(target=do_work, args=())
    t.start()
    # Running this on Anaconda runs the threads somewhat in parallel and finished very close by.
    # But used only 15-18% of the CPU, so ran 6 times the duration of the multiprocessing code.
