# Last updated: 10/10/2026, 8:04:43 PM
1class Solution:
2    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
3        p = {v : i for i,v in enumerate(nums)}
4        b,a = None,[-1,-1]
5        for i,v in enumerate(nums):
6            w = target - v
7            if w > v and w in p:
8                po = v*w
9                if b is None or po > b:
10                    b,a = po,[p[w],i]
11
12        return a
13        