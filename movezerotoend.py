def move_zeros_to_end(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros_count = len(nums) - len(non_zeros)
    return non_zeros + [0] * zeros_count