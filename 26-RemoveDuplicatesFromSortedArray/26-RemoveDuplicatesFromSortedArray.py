# Last updated: 3/22/2026, 12:46:11 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        point1 = 0

        for point2 in range(1, len(nums)):
            if nums[point2] != nums[point1]:
                point1 += 1
                nums[point1] = nums[point2]
        return point1 + 1