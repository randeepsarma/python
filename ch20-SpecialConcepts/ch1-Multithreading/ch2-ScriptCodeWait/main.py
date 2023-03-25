import threading
import time


start = time.perf_counter()
print(start)

i = 0


def do_something():
    global i

    print(f"Sleeping 1 second {i}")
    i += 1
    time.sleep(1)
    print(f"Done Sleeping...")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t1.start()
t2.start()

t1.join()  # stops execution of below finish
t2.join()  # stops execution of below finish

finish = time.perf_counter()
print(finish)
print(f"finished in {round(finish-start,2)} second(s)")
