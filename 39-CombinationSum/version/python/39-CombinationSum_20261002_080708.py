# Last updated: 10/2/2026, 8:07:08 AM
1class Solution:
2    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
3        result = []
4        path = []
5
6        def backtrack(start, remaining):
7            if remaining == 0:
8                result.append(path[:])
9                return
10
11            if remaining < 0:
12                return
13
14            for i in range(start, len(candidates)):
15                path.append(candidates[i])
16                backtrack(i, remaining - candidates[i])
17
18                path.pop()
19
20        backtrack(0, target)
21
22        return result