# Last updated: 7/29/2026, 1:33:03 AM
1from collections import Counter
2
3class Solution:
4    def smallestPalindrome(self, s: str) -> str:
5        cnt = Counter(s)
6
7        left = []
8        mid = ""
9
10        for ch in sorted(cnt):
11            left.append(ch * (cnt[ch] // 2))
12            if cnt[ch] % 2:
13                mid = ch
14
15        left = "".join(left)
16        return left + mid + left[::-1]