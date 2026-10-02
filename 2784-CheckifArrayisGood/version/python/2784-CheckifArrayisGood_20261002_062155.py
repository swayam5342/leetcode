# Last updated: 10/2/2026, 6:21:55 AM
1class Solution:
2    def isGood(self, nums: list[int]) -> bool:
3        n = max(nums)
4
5        if len(nums) != n + 1:
6            return False
7
8        count = [0] * (n + 1)
9
10        for num in nums:
11            count[num] += 1
12        for i in range(1, n):
13            if count[i] != 1:
14                return False
15        return count[n] == 2