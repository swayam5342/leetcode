# Last updated: 6/22/2026, 9:30:30 AM
1class Solution:
2    def maxNumberOfBalloons(self, text: str) -> int:
3        d = {
4            'b':0,
5            'a':0,
6            'l':0,
7            'o':0,
8            'n':0
9        }
10        for i in text:
11            if i in d:
12                d[i]+=1
13            else:
14                continue
15        
16        count  = float('inf')
17        for i in d:
18            if i in ('l','o'):
19                count = min(count , d[i]//2)
20            else:
21                count = min(count , d[i])
22        
23        return count