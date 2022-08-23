def partition(array, start, end):
    pivot = array[start]    # Select first element as pivot
    low = start + 1        # Index for forward search
    high = end          # Index for backward search

    while True:
        # Backward search:
        # Find first element less than or equal to pivot from the right
        while low <= high and array[high] >= pivot:
            high -= 1

        # Forward search:
        # Find first element greater than or equal to pivot from the left
        while low <= high and array[low] <= pivot:
            low += 1

        # Swap the two out of place elements, but break if the low and high indexes cross (which means the partition is finished)
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    # Swap the pivot with the element at the low index
    array[start], array[high] = array[high], array[start]
    print(array)

    return high

def quicksort(array, start, end):

    # Base case: If the array has 1 or 0 elements, it is already sorted
    if start >= end:
        return

    # Partition the array and get the index of the pivot
    pivot = partition(array, start, end)

    # Sort the left and right sides of the pivot
    quicksort(array, start, pivot - 1)
    quicksort(array, pivot + 1, end)



arr = [1,2,4,3]    # Test array
quicksort(arr, 0, len(arr) - 1)   # Sort the array
#print(arr)  # Print the sorted array
