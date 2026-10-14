def remove_duplicates(arr):
    if not arr:
        return 0
    
    # Pointer for unique elements
    i = 0
    
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
            
    return i + 1  # Length of unique elements array

# Example Usage:
# arr = [1, 1, 2, 2, 3, 4, 4]
# Output: Length = 4, Array becomes [1, 2, 3, 4, ...]