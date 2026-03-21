# Last updated: 3/22/2026, 12:45:47 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            r={}
            for i in range(len(s)):
                if s[i] in r:
                    r[s[i]]+=1
                else:
                    r[s[i]]=1
                if t[i] in r:
                    r[t[i]]+=-1
                else:
                    r[t[i]]=-1
            for i in r.values():
                if i!=0:
                    return False
            return True