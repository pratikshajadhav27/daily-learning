def singleNumber(nums) -> int:
    ans = 0
    for n in nums: ans ^= n
    return ans