# Last updated: 5/27/2026, 11:28:29 AM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        up = {}
4        lo = {}
5        count = 0 
6        for i, ch in enumerate(word):
7            if ch.islower():
8                lo[ch] = i
9            else:
10                if ch not in up:
11                    up[ch] = i
12    
13        for i in lo:
14            if i.upper() in up:
15                if lo[i] < up[i.upper()]:
16                    count+=1
17        
18        return count