class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        s_copy = s.lower()

        while i < j:
            temp_i = ord(s_copy[i])
            temp_j = ord(s_copy[j])
            if not ((temp_i >= 48 and temp_i <= 57) or (temp_i >= 97 and temp_i <= 122)):
                i += 1
                continue
            if not ((temp_j >= 48 and temp_j <= 57) or (temp_j >= 97 and temp_j <= 122)):
                j -= 1
                continue
            elif s_copy[i] == s_copy[j]:
                i += 1
                j -= 1
                continue
            else:
                return False

        return True