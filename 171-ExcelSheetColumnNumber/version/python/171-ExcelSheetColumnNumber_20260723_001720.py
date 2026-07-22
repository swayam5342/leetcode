# Last updated: 7/23/2026, 12:17:20 AM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0

        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            answer = answer * 26 + value

        return answer