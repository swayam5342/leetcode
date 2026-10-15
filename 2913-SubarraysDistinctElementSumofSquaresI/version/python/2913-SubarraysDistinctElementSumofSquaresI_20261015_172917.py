# Last updated: 10/15/2026, 5:29:17 PM
1
2from typing import List
3
4class Solution:
5    def sumCounts(self, nums: List[int]) -> int:
6        n = len(nums)
7        total = 0
8
9        for i in range(n):
10            seen = set()
11
12            for j in range(i, n):
13                seen.add(nums[j])
14                distinct = len(seen)
15                total += distinct * distinct
16
17        return total