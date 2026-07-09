# Last updated: 7/9/2026, 8:30:58 PM
1class Solution:
2    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
3        comp = [0] * n
4        comp_id = 0
5
6        for i in range(1, n):
7            if nums[i] - nums[i - 1] > maxDiff:
8                comp_id += 1
9            comp[i] = comp_id
10        return [comp[u] == comp[v] for u, v in queries]