def singleNumber(nums: list) -> int:
    unique = 0
    for num in nums:
        unique ^= num  # XOR operation cancels out duplicate numbers
    return unique

# Example: nums = [4, 1, 2, 1, 2] -> Output: 4