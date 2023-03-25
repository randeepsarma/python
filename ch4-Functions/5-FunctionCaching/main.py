import time
from functools import lru_cache


# the value of last 3 calls will b saved,it is generally used when values repeat
@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("Now running some work")
    some_work(3)  # takes 3 seconds
    some_work(1)
    some_work(2)  # caches this value as maxsize is 3
    some_work(2)  # caches this value as maxsize is 3
    some_work(4)  # caches this value as maxsize is 3
    print("Done... Calling again")
    some_work(3)  # runs right after withou taking 3 seconds
    print("Called again")
