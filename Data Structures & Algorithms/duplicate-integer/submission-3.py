class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_dict = {}
        for i in nums:
            temp_dict[i] = temp_dict.get(i, 0) + 1

        if bool(temp_dict.values()) and max(temp_dict.values()) > 1:
            return True

        else:
            return False