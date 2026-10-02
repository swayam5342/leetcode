# Last updated: 10/2/2026, 7:49:14 AM
1class Solution:
2    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4
5        result = []
6        path = []
7        used = [False] * len(nums)
8
9        def backtrack():
10            if len(path) == len(nums):
11                result.append(path[:])
12                return
13
14            for i in range(len(nums)):
15
16                if used[i]:
17                    continue
18                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
19                    continue
20
21                path.append(nums[i])
22                used[i] = True
23
24                backtrack()
25
26                used[i] = False
27                path.pop()
28
29        backtrack()
30
31        return result