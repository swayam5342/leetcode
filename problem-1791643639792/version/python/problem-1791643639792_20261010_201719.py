# Last updated: 10/10/2026, 8:17:19 PM
1from math import gcd
2from itertools import groupby
3
4class Solution:
5    def resilientSubarray(self, nums: list[int], k: int) -> int:
6        ans = 1
7        for r, grp in groupby(x % k for x in nums):
8            m = sum(1 for _ in grp)
9            g = k // gcd(r,k)
10            l = 1 + ((m-1)//g)*g
11            if l > ans:
12                ans = l
13
14        return ans