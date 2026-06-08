# Last updated: 6/8/2026, 10:09:27 AM
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        l=[]
4        h=[]
5        count = 0
6        for i in nums:
7            if i < pivot:
8                l.append(i)
9            elif i > pivot:
10                h.append(i)
11            else:
12                count+=1
13        return l + [pivot]*count + h