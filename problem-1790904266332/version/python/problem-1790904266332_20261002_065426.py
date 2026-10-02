# Last updated: 10/2/2026, 6:54:26 AM
1from collections import Counter
2
3class Solution:
4    def customSortString(self, order: str, s: str) -> str:
5        count = Counter(s)
6        result = []
7        for char in order:
8            if char in count:
9                result.append(char * count[char])
10                del count[char]
11        for char, freq in count.items():
12            result.append(char * freq)
13
14        return ''.join(result)