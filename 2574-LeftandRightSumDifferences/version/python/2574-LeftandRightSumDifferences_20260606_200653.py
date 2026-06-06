# Last updated: 6/6/2026, 8:06:53 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        l = [0 for _ in range(len(nums))]
4        r = [0 for _ in range(len(nums))]
5        result = [0 for _ in range(len(nums))]
6        for i in range(len(nums)):
7            l[i] = (sum(nums[:i]))
8            r[i] = (sum(nums[i+1:]))
9            result[i] = abs(r[i]-l[i])
10        
11        return result