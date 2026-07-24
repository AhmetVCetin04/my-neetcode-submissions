class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_copy = list(t)

        for i in s:
            if bool(t_copy) == False:
                return 0
            if t_copy[0] == i:
                t_copy.pop(0)
                continue
        
        return len(t_copy)