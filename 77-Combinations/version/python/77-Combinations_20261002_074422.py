# Last updated: 10/2/2026, 7:44:22 AM
1class Solution:
2    def combine(self, n: int, k: int) -> list[list[int]]:
3        result = []
4        path = []
5
6        def backtrack(start):
7            if len(path) == k:
8                result.append(path[:])
9                return
10
11            for num in range(start, n + 1):
12                path.append(num)
13
14                backtrack(num + 1)
15
16                path.pop()
17
18        backtrack(1)
19
20        return result