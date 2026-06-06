# Last updated: 6/6/2026, 8:05:21 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        l = []
4        r = []
5        result = [0 for _ in range(len(nums))]
6        for i in range(len(nums)):
7            l.append(sum(nums[:i]))
8            r.append(sum(nums[i+1:]))
9        
10        for i in range(len(nums)):
11            result[i] = abs(r[i]-l[i])
12        
13        return result