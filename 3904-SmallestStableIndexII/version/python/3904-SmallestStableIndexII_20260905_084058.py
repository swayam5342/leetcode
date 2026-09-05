# Last updated: 9/5/2026, 8:40:58 AM
1class Solution:
2    def firstStableIndex(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        suffix_min = [0] * n
5        suffix_min[n - 1] = nums[n - 1]
6
7        for i in range(n - 2, -1, -1):
8            suffix_min[i] = min(nums[i], suffix_min[i + 1])
9        prefix_max = nums[0]
10
11        for i in range(n):
12            prefix_max = max(prefix_max, nums[i])
13
14            if prefix_max - suffix_min[i] <= k:
15                return i
16
17        return -1