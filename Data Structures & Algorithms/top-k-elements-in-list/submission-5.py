class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the following dict:
        #dictionary{0: freqOf0, 1:FreqOf1, ... , 9:FreqOF9}
        #sort the dictionary by greatest frequency
        #return first k sorted key values
        
        frequency = {}

        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1

        return(sorted(frequency, reverse=True, key=frequency.get)[0:k])
        
