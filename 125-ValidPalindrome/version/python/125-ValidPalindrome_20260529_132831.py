# Last updated: 5/29/2026, 1:28:31 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left, right = 0, len(s) - 1
4
5        while left < right:
6            while left < right and not s[left].isalnum():
7                left += 1
8
9            while left < right and not s[right].isalnum():
10                right -= 1
11
12            if s[left].lower() != s[right].lower():
13                return False
14
15            left += 1
16            right -= 1
17
18        return True