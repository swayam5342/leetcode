# Last updated: 7/23/2026, 12:17:03 AM
1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        t = 0
4        n =  {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
5        for i in columnTitle:
6            t=t*26 + n[i]
7        return t