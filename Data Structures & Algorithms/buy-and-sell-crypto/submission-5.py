class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0

        for r in range(1, len(prices)):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            res = max(res, diff)

        return res