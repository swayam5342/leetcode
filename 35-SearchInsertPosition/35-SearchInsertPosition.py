# Last updated: 3/22/2026, 12:46:07 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)
        while l<h:
            mid = (l+h)//2
            if (nums[mid]>target):
                h=mid
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return (l+h)//2
