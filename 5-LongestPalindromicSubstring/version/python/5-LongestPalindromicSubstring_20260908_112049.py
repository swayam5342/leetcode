# Last updated: 9/8/2026, 11:20:49 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if len(s) < 2:
4            return s
5
6        start = 0
7        end = 0
8
9        def expand(left, right):
10            while left >= 0 and right < len(s) and s[left] == s[right]:
11                left -= 1
12                right += 1
13            return left + 1, right - 1
14
15        for i in range(len(s)):
16            l1, r1 = expand(i, i)
17            l2, r2 = expand(i, i + 1)
18
19            if r1 - l1 > end - start:
20                start, end = l1, r1
21
22            if r2 - l2 > end - start:
23                start, end = l2, r2
24
25        return s[start:end + 1]