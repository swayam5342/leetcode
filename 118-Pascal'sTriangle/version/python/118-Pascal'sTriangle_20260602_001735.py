# Last updated: 6/2/2026, 12:17:35 AM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        triangle = []
4
5        for i in range(numRows):
6            numRows = [1] * (i + 1)
7
8            for j in range(1, i):
9                numRows[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
10
11            triangle.append(numRows)
12
13        return triangle