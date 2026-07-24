class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if x.get(i) is None:
                x[i] = i
            else:
                return True
        return False