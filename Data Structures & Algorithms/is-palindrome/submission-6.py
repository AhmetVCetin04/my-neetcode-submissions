import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        temp = []

        for i in s_lower:
            if not ((48 <= ord(i) and ord(i) <= 57) or (97 <= ord(i) and ord(i) <= 122)):
                continue
            temp.append(i)

        l, r = 0, len(temp) - 1

        while l < r:
            if temp[l] == temp[r]:
                l += 1
                r -= 1
                continue
            else:
                return False

        return True