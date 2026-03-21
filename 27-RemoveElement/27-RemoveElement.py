# Last updated: 3/22/2026, 12:46:09 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        point1 = 0
        for point2 in range(len(nums)):
            if nums[point2] != val:
                nums[point1] = nums[point2]
                point1 += 1
        return point1
