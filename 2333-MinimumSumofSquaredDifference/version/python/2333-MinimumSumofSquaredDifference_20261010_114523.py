# Last updated: 10/10/2026, 11:45:23 AM
1from typing import List
2
3class Solution:
4    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
5        diff = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
6        k = k1 + k2
7        n = len(diff)
8
9        if sum(diff) <= k:
10            return 0
11
12        diff.append(0)
13        level = diff[0]
14        i = 0                      
15        while True:
16            nxt = diff[i + 1]
17            cost = (level - nxt) * (i + 1)
18            if k >= cost:
19                k -= cost
20                level = nxt
21                i += 1
22            else:
23                drop, rem = divmod(k, i + 1)
24                level -= drop
25                top = rem * (level - 1) ** 2 + (i + 1 - rem) * level ** 2
26                return top + sum(x * x for x in diff[i + 1:n])