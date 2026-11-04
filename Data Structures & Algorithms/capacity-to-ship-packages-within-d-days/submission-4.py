class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = float("inf")

        while left <= right:
            mid = (left + right) // 2
            
            day = 1
            curSum = 0
            for w in weights:
                curSum += w
                if curSum > mid:
                    day += 1
                    curSum = w

            if day <= days:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res

            
                




