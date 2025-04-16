# Binary Search O(log n)
import random

# iteritive


def binary_search(array, target):
    first = 0
    last = len(array) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return f"Target({target}) not found."

# recursive


def recursive_binary_search(array, target):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2

        if array[midpoint] == target:
            return True
        else:
            if array[midpoint] < target:
                return recursive_binary_search(array[midpoint+1:], target)
            else:
                return recursive_binary_search(array[:midpoint], target)


def main():
    array = []
    for i in range(10000):
        array.append(random.randrange(0, 10001))
        array.sort()
    print(recursive_binary_search(array, 55))


main()
