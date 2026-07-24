class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        valueHash = {}
        for index in range(len(nums)):
            valueHash[nums[index]] = valueHash.get(nums[index]) + 1 if valueHash.get(nums[index]) is not None else 1

        return max(valueHash, key=valueHash.get)