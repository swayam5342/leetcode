# Last updated: 6/6/2026, 8:07:35 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        result = [0 for _ in range(len(nums))]
4        for i in range(len(nums)):
5            l= sum(nums[:i])
6            r= sum(nums[i+1:])
7            result[i] = abs(r-l)
8        
9        return result