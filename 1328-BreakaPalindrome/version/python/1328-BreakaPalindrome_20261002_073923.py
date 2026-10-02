# Last updated: 10/2/2026, 7:39:23 AM
1class Solution:
2    def breakPalindrome(self, palindrome: str) -> str:
3        n = len(palindrome)
4        if n == 1:
5            return ""
6        palindrome = list(palindrome)
7        for i in range(n // 2):
8            if palindrome[i] != 'a':
9                palindrome[i] = 'a'
10                return ''.join(palindrome)
11        palindrome[-1] = 'b'
12
13        return ''.join(palindrome)