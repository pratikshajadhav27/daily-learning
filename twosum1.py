def twoSum(nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# Example: nums = [2, 7, 11, 15], target = 9 -> Output: [0, 1]