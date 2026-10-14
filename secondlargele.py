def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Second largest doesn't exist
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None

# Example Usage:
# arr = [12, 35, 1, 10, 34, 1]
# Output: 34