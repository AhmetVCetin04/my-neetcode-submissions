class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, j in zip(range(len(s)), range(len(s)-1, -1, -1)):
            if i == j:
                return
            if i + 1 == j:
                s[i], s[j] = s[j], s[i]
                return
            s[i], s[j] = s[j], s[i]

        return