class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest_str_len = 201
        for i in strs:
            if len(i) < shortest_str_len:
                shortest_str_len = len(i)

        check_against = strs[0]
        new_strs = strs[1:]

        for i in range(shortest_str_len):
            for j in strs:
                if check_against[i] != j[i]:
                    return j[0:i]

        return check_against[0:shortest_str_len]
        