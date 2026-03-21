# Last updated: 3/22/2026, 12:45:42 AM
class Solution:
    def binaryGap(self, n: int) -> int:
        x = bin(n)
        s = str(x)
        m = 0
        ind = -1
        f ='1'
        for i in range(len(s)):
            if(s[i] == f):
                if(ind !=-1):
                    m = max((i - ind),m)
                ind =i
        return m