def reverseArray(arr):
    # Use two pointers to swap elements in-place
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap the elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1