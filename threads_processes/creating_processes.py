import multiprocessing

from multiprocessing import Process


def do_work():
    print("Starting work")
    i = 0
    for _ in range(200000000):
        i += 1
    print("Finished work")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    for _ in range(12):
        p = Process(target=do_work, args=())
        p.start()
    # Runs exactly parallely in Anaconda and finish at almost the same time. Took 100% of the CPU.
