# Last updated: 9/3/2026, 2:52:00 PM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        odds = [x for x in nums1 if x % 2 == 1]
4        evens = [x for x in nums1 if x % 2 == 0]
5        even_target_ok = (len(odds) == 0)
6        if len(evens) == 0:
7            odd_target_ok = True
8        elif len(odds) == 0:
9            odd_target_ok = False
10        else:
11            odd_target_ok = min(odds) < min(evens)
12
13        return even_target_ok or odd_target_ok