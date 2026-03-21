# Last updated: 3/22/2026, 12:45:44 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i - zero_count] = nums[i]
            else:
                zero_count += 1
        for i in range(len(nums) - zero_count, len(nums)):
            nums[i] = 0