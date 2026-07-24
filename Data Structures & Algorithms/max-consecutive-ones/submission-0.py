class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        best = 0
        current = 0

        for i in nums:
            if i == 0:
                current = 0
                continue

            if i == 1:
                current = current + 1
                if current > best:
                    best = current

        return best