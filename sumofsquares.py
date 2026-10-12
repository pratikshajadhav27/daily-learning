def sumOfSquares(nums: list[int]) -> int:
    n = len(nums)
    total_sum = 0
    
    # Iterate from 1 to n to handle 1-indexing as specified in the problem
    for i in range(1, n + 1):
        if n % i == 0:
            # nums[i - 1] maps the 1-indexed position 'i' to Python's 0-indexed list
            val = nums[i - 1]
            total_sum += val * val
            
    return total_sum