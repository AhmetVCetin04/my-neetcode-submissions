class Solution:
    def scoreOfString(self, s: str) -> int:
        total_diff = 0
        for i in range(len(s) - 1):
            total_diff += abs(ord(s[i]) - ord(s[i+1]))

        return total_diff