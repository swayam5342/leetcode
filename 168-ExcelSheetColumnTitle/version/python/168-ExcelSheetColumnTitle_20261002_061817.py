# Last updated: 10/2/2026, 6:18:17 AM
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        result = ""
4
5        while columnNumber > 0:
6            columnNumber -= 1
7
8            remainder = columnNumber % 26
9            result += chr(ord('A') + remainder)
10
11            columnNumber //= 26
12
13        return result[::-1]