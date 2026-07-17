class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            hour = 0

            for pile in piles:
                hour += math.ceil(float(pile) / m)

            if hour <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res