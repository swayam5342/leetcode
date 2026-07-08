# Last updated: 7/8/2026, 11:47:19 PM
1class Solution:
2    def addDigits(self, num: int) -> int:
3        def add(nums):
4            t = 0
5            while nums>0:
6                t+= nums%10
7                nums = nums//10
8            return t
9        while num>9:
10            num = add(num)
11        return num