# Last updated: 7/22/2026, 5:23:13 AM
1class Solution:
2    def judgeSquareSum(self, c: int) -> bool:
3        # for this problem we are going to use two pointer
4
5        l = [i*i for i in range(int(sqrt(c)+1))]
6
7        low = 0
8        high = len(l)-1
9
10        while (low <= high):
11            t = l[low]+l[high]
12
13            if t < c:
14                low+=1
15            elif t > c:
16                high-=1
17            else:
18                return True
19        
20        return False