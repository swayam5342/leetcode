# Last updated: 10/2/2026, 6:17:37 AM
1class Solution:
2    def generateMatrix(self, n: int) -> list[list[int]]:
3        matrix = [[0] * n for _ in range(n)]
4
5        top = 0
6        bottom = n - 1
7        left = 0
8        right = n - 1
9
10        num = 1
11
12        while top <= bottom and left <= right:
13            for col in range(left, right + 1):
14                matrix[top][col] = num
15                num += 1
16            top += 1
17            for row in range(top, bottom + 1):
18                matrix[row][right] = num
19                num += 1
20            right -= 1
21            if top <= bottom:
22                for col in range(right, left - 1, -1):
23                    matrix[bottom][col] = num
24                    num += 1
25                bottom -= 1
26            if left <= right:
27                for row in range(bottom, top - 1, -1):
28                    matrix[row][left] = num
29                    num += 1
30                left += 1
31        return matrix