class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1. brute force
        nums_copy = list.copy(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product = product * nums[j]
            nums_copy[i]=int(product)

        return nums_copy

        2. with division

            
        '''

        product = 1
        num_of_zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_of_zeroes = num_of_zeroes + 1
                continue
            product = product * nums[i]

        if num_of_zeroes >= 2:
            return([0] * len(nums))

        nums_copy = list.copy(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums_copy[i] = product
                continue
            if num_of_zeroes > 0:
                nums_copy[i] = 0
                continue
            nums_copy[i] = int(product / nums[i])

        return nums_copy
