# Last updated: 10/2/2026, 7:54:49 AM
1class Solution:
2    def permute(self, nums: list[int]) -> list[list[int]]:
3        result = []
4        path = []
5        used = [False] * len(nums)
6
7        def backtrack():
8            if len(path) == len(nums):
9                result.append(path[:])
10                return
11
12            for i in range(len(nums)):
13                if used[i]:
14                    continue
15
16                path.append(nums[i])
17                used[i] = True
18
19                backtrack()
20
21                used[i] = False
22                path.pop()
23
24        backtrack()
25
26        return result