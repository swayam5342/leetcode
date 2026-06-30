# Last updated: 6/30/2026, 10:04:44 AM
1from itertools import permutations
2class Solution:
3    def numberOfSubstrings(self, s: str) -> int:
4        count = {'a': 0, 'b': 0, 'c': 0}
5        left = 0
6        ans = 0
7
8        for right in range(len(s)):
9            count[s[right]] += 1
10
11            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
12                ans += len(s) - right
13                count[s[left]] -= 1
14                left += 1
15
16        return ans