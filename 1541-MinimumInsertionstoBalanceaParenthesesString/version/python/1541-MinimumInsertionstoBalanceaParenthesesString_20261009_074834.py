# Last updated: 10/9/2026, 7:48:34 AM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        insertions = 0
4        open_needed = 0
5
6        for ch in s:
7            if ch == '(':
8                if open_needed % 2 == 1:
9                    insertions += 1
10                    open_needed -= 1
11
12                open_needed += 2
13
14            else:
15                open_needed -= 1
16                if open_needed < 0:
17                    insertions += 1
18                    open_needed = 1
19        return insertions + open_needed