# Last updated: 5/26/2026, 6:56:39 PM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        lower = set()
4        upper = set()
5
6        for ch in word:
7            if ch.islower():
8                lower.add(ch)
9            else:
10                upper.add(ch)
11
12        count = 0
13
14        for ch in lower:
15            if ch.upper() in upper:
16                count += 1
17
18        return count
19