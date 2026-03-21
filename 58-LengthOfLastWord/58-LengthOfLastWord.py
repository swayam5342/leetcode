# Last updated: 3/22/2026, 12:46:08 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip().split()
        return len(l[-1])
        