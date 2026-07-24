class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr_len = len(nums)
        
        nums.append('_')

        i = 0
        val_count = 0

        while nums[i] != '_':
            if nums[i] == val:
                nums.pop(i)
                val_count += 1
            else:
                i += 1

        nums.pop()

        return arr_len - val_count


