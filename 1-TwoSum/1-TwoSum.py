# Last updated: 3/22/2026, 12:46:23 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        re = {}
        for i in range(len(nums)):
            r = target-nums[i]
            if r in re:
                return [re[r],i]
            re[nums[i]]=i
        return []