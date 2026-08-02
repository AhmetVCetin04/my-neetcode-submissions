class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while j - i > 3:
            if nums[(j-i) // 2] > target:
                j -= (j-i) // 2
            elif nums[(j-i) // 2] < target:
                i += (j-i) // 2
            else:
                return (j-i)//2

        for a in range(i, j+1):
            if nums[a] == target:
                return a

        return -1
    