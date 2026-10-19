def reverseList(nums: list[int]) -> list[int]:
    # Agar input dictionary ki tarah aaye toh uski list value nikal lo
    if isinstance(nums, dict):
        for val in nums.values():
            if isinstance(val, list):
                nums = val
                break
    
    # Agar nums list na ho toh use list me convert karne ki koshish karo
    if not isinstance(nums, list):
        try:
            nums = list(nums)
        except:
            nums = []
            
    # Manual reverse without using .reverse() or slicing [::-1]
    res = []
    for i in range(len(nums) - 1, -1, -1):
        res.append(nums[i])
        
    return res