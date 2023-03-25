import threading
import time


start = time.perf_counter()
print(start)

i = 0


def do_something(seconds):
    global i

    print(f"Sleeping {seconds} second {i}")
    i += 1
    time.sleep(seconds)
    print(f"Done Sleeping...")


threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)
print(threading.active_count())

for thread in threads:
    thread.join()


finish = time.perf_counter()
print(finish)
print(f"finished in {round(finish-start,2)} second(s)")
