# Last updated: 6/16/2026, 7:43:05 PM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5
6        rows = [""] * numRows
7        curr_row = 0
8        direction = 1 
9        for ch in s:
10            rows[curr_row] += ch
11
12            if curr_row == 0:
13                direction = 1
14            elif curr_row == numRows - 1:
15                direction = -1
16
17            curr_row += direction
18
19        return "".join(rows)