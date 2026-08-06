class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        greatest_profit = 0
        
        for i in prices:
            if i < lowest_price:
                lowest_price = i
            
            if i - lowest_price > greatest_profit:
                greatest_profit = i - lowest_price
            
        return greatest_profit