# Last updated: 10/22/2026, 3:30:46 PM
1from collections import deque
2from typing import List
3
4class Solution:
5    def minOperations(self, nums: List[int]) -> int:
6        n = len(nums)
7        k0 = nums[0]
8
9        if all(nums[i] == (i + k0) % n for i in range(n)):
10            s0 = 1
11        elif all(nums[i] == (-i + k0) % n for i in range(n)):
12            s0 = -1
13        else:
14            return -1
15        def sid(s, k):
16            return (0 if s == 1 else 1) * n + k
17
18        dist = [-1] * (2 * n)
19        start = sid(s0, k0)
20        dist[start] = 0
21        q = deque([(s0, k0)])
22
23        while q:
24            s, k = q.popleft()
25            d = dist[sid(s, k)]
26            if s == 1 and k == 0:
27                return d
28            ns, nk = s, (k + s) % n
29            if dist[sid(ns, nk)] == -1:
30                dist[sid(ns, nk)] = d + 1
31                q.append((ns, nk))
32            ns, nk = -s, (k + s * (n - 1)) % n
33            if dist[sid(ns, nk)] == -1:
34                dist[sid(ns, nk)] = d + 1
35                q.append((ns, nk))
36
37        return -1