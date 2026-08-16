class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxProfit = 0, 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
        