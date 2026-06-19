# Last updated: 6/19/2026, 3:40:32 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        count = 0
4        ma = 0
5        for i in gain:
6            count+=i
7            ma =max(count,ma)
8        return ma