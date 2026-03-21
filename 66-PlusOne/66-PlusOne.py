# Last updated: 3/22/2026, 12:46:03 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i,num in enumerate(digits):
            n+=num*pow(10,(len(digits)-i-1))
        n=n+1
        l = str(n)
        k=[]
        for i in l:
            k.append(i)
        l = [int(x) for x in k]
        return l