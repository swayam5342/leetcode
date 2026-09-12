# Last updated: 9/12/2026, 8:14:36 PM
1from collections import defaultdict
2
3class Solution:
4    def countSpecialIntegers(self, nums: list[int]) -> int:
5        p = defaultdict(list)
6        for i in range(len(nums)):
7            p[nums[i]].append(i)
8
9        x = 0
10        for i in p:
11            if(len(p[i])>=3):
12                g = p[i][1] - p[i][0]
13                flag = True
14                for j in range(2,len(p[i])):
15                    if p[i][j] - p[i][j-1] != g:
16                        flag = False
17                        break
18                if flag:
19                    x+=1
20        return x