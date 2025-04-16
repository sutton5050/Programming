# Time Complexity = O(n²)

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        # Track if any swaps are made during this pass
        swapped = False
        for j in range(0, n - i - 1):  # Reduce the range with each pass
            if list[j] > list[j + 1]:
                # Swap the elements
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        # If no swaps were made, the list is already sorted
        if not swapped:
            break
    return list


# Test the function
print(bubble_sort([2, 3, 8, 9, 3, 30, 6, 2]))
