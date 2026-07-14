class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res, profit = 0, 0, 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[l] > prices[r]:
                l = r

        return res
