def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
        
    # Bitwise AND operation (O(1) time complexity)
    return (n & (n - 1)) == 0

# Example: n = 16 -> Output: True, n = 18 -> Output: False