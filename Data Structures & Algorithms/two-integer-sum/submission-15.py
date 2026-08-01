class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dih = {}
        
        for i, n in enumerate(nums):
            my_dih[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_dih and my_dih[diff] != i:
                return [i, my_dih[diff]]

        return []