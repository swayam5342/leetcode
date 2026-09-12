# Last updated: 9/12/2026, 3:08:46 PM
1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        row = [1]
4
5        for i in range(rowIndex):
6            new_row = [1]
7
8            for j in range(len(row) - 1):
9                new_row.append(row[j] + row[j + 1])
10
11            new_row.append(1)
12            row = new_row
13
14        return row