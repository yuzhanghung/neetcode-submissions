class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            water = min(heights[l], heights[r]) * abs(r - l)
            res = max(water, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
