"""
Best Time to Buy Stock
    EASY (Thurs 8 Sept 2022)
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
  
        maxProfit = 0
        highestPrice = 0
    
        # Look through list backwards to find the highestPrice 
        # and the maxProfit by subtracting with prices on days before the highestPrice
        for price in reversed(prices):
            if price > highestPrice:
                # Found new highestPrice 
                highestPrice = price

            profit = highestPrice - price
            
            if profit > maxProfit:
                # Found new maxProfit
                maxProfit = profit

        return maxProfit
