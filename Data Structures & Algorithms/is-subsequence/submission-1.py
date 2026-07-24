class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        s_c = 0

        for t_c in t:
            if t_c == s[s_c]:
                s_c = s_c + 1
            if s_c == len(s):
                return True

        return False