def mean(arr):
    # Calculate the sum of elements divided by the total number of elements, then take the floor value
    total_sum = sum(arr)
    n = len(arr)
    return total_sum // n