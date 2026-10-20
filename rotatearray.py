def rotate(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]