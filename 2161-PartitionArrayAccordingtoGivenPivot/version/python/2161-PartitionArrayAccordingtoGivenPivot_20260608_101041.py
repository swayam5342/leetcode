# Last updated: 6/8/2026, 10:10:41 AM
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        l=[]
4        eq=[]
5        h=[]
6        count = 0
7        for i in nums:
8            if i < pivot:
9                l.append(i)
10            elif i > pivot:
11                h.append(i)
12            else:
13                eq.append(i)
14        return l + eq + h