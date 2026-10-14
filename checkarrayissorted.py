def isArraySorted(arr):
    # Check if every element is smaller than or equal to its next value
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True