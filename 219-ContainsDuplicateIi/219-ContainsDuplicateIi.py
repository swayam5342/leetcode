# Last updated: 3/22/2026, 12:45:49 AM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r = {}
        for i,v in enumerate(nums):
            if(v in r):
                if(abs(r[v]-i)<=k ):
                    return True
            r[v]=i
        return False