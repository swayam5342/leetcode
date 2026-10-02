# Last updated: 10/2/2026, 6:57:29 AM
1class Solution:
2    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
3        nums.sort()
4        n = len(nums)
5        dp = [1] * n
6        parent = [-1] * n
7        max_len = 1
8        max_index = 0
9        for i in range(n):
10            for j in range(i):
11                if nums[i] % nums[j] == 0:
12                    if dp[j] + 1 > dp[i]:
13                        dp[i] = dp[j] + 1
14                        parent[i] = j
15
16            if dp[i] > max_len:
17                max_len = dp[i]
18                max_index = i
19        result = []
20        while max_index != -1:
21            result.append(nums[max_index])
22            max_index = parent[max_index]
23
24        return result[::-1]