# Last updated: 10/2/2026, 6:48:18 AM
1from collections import Counter
2
3class Solution:
4    def frequencySort(self, s: str) -> str:
5        count = Counter(s)
6
7        result = ""
8
9        for char, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
10            result += char * freq
11
12        return result