# Last updated: 6/29/2026, 6:29:19 PM
1class Solution:
2    def numOfStrings(self, patterns: List[str], word: str) -> int:
3        count  = 0
4        for i in patterns:
5            if i in word:
6                count+=1
7        
8        return count