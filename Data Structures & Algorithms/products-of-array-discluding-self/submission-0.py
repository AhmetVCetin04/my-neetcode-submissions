class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1. brute force
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product = product * nums[j]
            nums[i]=product
        '''

        nums_copy = list.copy(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product = product * nums[j]
            nums_copy[i]=int(product)

        return nums_copy