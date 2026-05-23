# Last updated: 5/23/2026, 7:08:48 PM
1class Solution:
2    def check(self, nums: List[int]) -> bool:
3        n=0
4        for i in range(len(nums)):
5            if  nums[(i + 1) % len(nums)] < nums[i]:
6                n+=1
7            if n > 1:
8                return False
9        else:
10            return True