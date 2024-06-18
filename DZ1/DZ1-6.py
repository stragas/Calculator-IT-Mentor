def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test the binary search algorithm
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14

result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the array")


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to check if any swapping is done in this pass
        swapped = False

        # Last i elements are already sorted, so we don't need to consider them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

    return arr


# Test the Bubble Sort algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)