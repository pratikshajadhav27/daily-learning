class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        
        # Non-zero elements ko aage shift karo
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
                
        # Baaki bachi jagah par 0 fill kar do
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1