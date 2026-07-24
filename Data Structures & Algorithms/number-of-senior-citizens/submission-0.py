class Solution:
    def countSeniors(self, details: List[str]) -> int:

        num_of_passengers = 0
        
        for i in details:
            if int(i[11:13]) > 60:
                num_of_passengers = num_of_passengers + 1

        return num_of_passengers