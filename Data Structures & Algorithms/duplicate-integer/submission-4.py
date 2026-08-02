class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}

        for i in range(len(nums)):
            temp[nums[i]] = temp.get(nums[i], 0) + 1

        for a in temp.values():
            if a >= 2:
                return True
        else:
            return False