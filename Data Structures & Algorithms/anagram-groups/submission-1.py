class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordHashMap = [dict() for _ in strs]

        for w, dictionary in zip(strs, wordHashMap):
            for c in w:
                dictionary[c] = dictionary.get(c, 0) + 1

        groups = []
        used = set()

        for i in range(len(wordHashMap)):
            if i in used:
                continue
            
            current_group = [strs[i]]
            used.add(i)

            for j in range(i+1, len(wordHashMap)):
                if wordHashMap[i] == wordHashMap[j]:
                    current_group.append(strs[j])
                    used.add(j)

            groups.append(current_group)

        return groups
