class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bought = prices[0]
        sold = 0

        for i in range(1, len(prices)):
            if prices[i] > sold:
                sold = prices[i]
                maxProfit = max(maxProfit, sold - bought)

            if prices[i] <= bought:
                bought = prices[i]
                sold = 0
        
        return maxProfit