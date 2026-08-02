class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for c_s in s:
            dict_s[c_s] = dict_s.get(c_s, 0) + 1

        for c_t in t:
            dict_t[c_t] = dict_t.get(c_t, 0) + 1

        if dict_s == dict_t:
            return True
        else:
            return False