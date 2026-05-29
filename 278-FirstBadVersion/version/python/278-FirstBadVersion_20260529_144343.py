# Last updated: 5/29/2026, 2:43:43 PM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        l = 1
7        h = n
8        while l < h:
9            m = (l+h)//2
10            r = isBadVersion(m)
11            if r:
12                h = m
13            if not r:
14                l = m+1
15        return l
16            