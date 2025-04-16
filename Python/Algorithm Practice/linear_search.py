# Linear Search O(n)
import random
import time


def main(n):
    list = []
    for i in range(100000):
        list.append(random.randrange(0, 100001))
    # print(list)
    print(linear_search(list, n))


def linear_search(list, n):
    for index, i in enumerate(list):
        if i == n:
            return f"Looking for ({n}), Found at index {index}."
    return f"{n} not found"


start_time = time.perf_counter()
main(5)
end_time = time.perf_counter()
print(f"This took {round(start_time - end_time, 10)}ms")
