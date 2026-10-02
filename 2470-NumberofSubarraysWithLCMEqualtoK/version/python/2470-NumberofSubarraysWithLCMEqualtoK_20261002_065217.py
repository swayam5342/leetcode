# Last updated: 10/2/2026, 6:52:17 AM
1from math import gcd
2
3class Solution:
4    def subarrayLCM(self, nums: list[int], k: int) -> int:
5        ans = 0
6
7        for i in range(len(nums)):
8            lcm = 1
9
10            for j in range(i, len(nums)):
11                if k % nums[j] != 0:
12                    break
13
14                lcm = lcm * nums[j] // gcd(lcm, nums[j])
15
16                if lcm == k:
17                    ans += 1
18                elif lcm > k:
19                    break
20
21        return ans