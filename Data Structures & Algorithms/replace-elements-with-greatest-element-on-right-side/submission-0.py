class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_copy = list.copy(arr)

        largest_val_thus_far = -1

        for i in range(len(arr_copy) - 1, -1, -1):
            if arr_copy[i] > largest_val_thus_far:
                largest_val_thus_far, arr_copy[i] = arr_copy[i], largest_val_thus_far
            elif arr_copy[i] < largest_val_thus_far:
                arr_copy[i] = largest_val_thus_far
                
        return(arr_copy)