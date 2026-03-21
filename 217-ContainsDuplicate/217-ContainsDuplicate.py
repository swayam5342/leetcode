# Last updated: 3/22/2026, 12:45:51 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h =set()
        for i in nums:
            if (i in h):
                return True
            h.add(i)
        return False
        