# Last updated: 5/29/2026, 1:21:16 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        num = 0 
4        count = 0
5        for i in nums:
6            if count == 0:
7                num = i
8            if num == i:
9                count +=1
10            else:
11                count-=1
12        return num