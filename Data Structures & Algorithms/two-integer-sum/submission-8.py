class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = numbers.get(nums[i], 0) + 1

        for i in range(len(nums)):
            if numbers.get(target - nums[i], 0) != 0:
                for j in range(i+1,len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i, j]
