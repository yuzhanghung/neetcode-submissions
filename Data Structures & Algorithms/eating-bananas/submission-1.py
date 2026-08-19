class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r

        while l <= r:
            k = (l + r) // 2
            hr = 0

            for p in piles:
                hr += math.ceil(float(p) / k)

            if hr <= h:
                minK = min(k, minK)
                r = k - 1
            else:
                l = k + 1
        
        return minK

