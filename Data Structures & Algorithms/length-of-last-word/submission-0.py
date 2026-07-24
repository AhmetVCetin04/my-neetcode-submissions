class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spaces_ended = False
        word_length = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and spaces_ended == False:
                continue
            if s[i] == " " and spaces_ended == True:
                return word_length
            spaces_ended = True
            word_length = word_length + 1

        return word_length