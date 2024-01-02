class Solution:
    # this is a better solution as it iterates a price list just once 
    # every iteration you update min price and max profit with new data and return max profit at the end
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                x = price - min_price
                if x > maxProfit:
                    maxProfit = x
        return maxProfit
    
    # this solution with a time limit exeeded at large input as it is o(n^2) 
    # for i in range(len(prices)-1):
    #     max = prices[i+1]
    #     for j in range(i+1, len(prices)):
    #         if prices[j] > max:
    #             max = prices[j]

    #     prices[i] = max - prices[i]
    #     if prices[i] > maxProfit:
    #         maxProfit = prices[i]
