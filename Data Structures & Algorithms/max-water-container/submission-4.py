class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            width = r - l
            if heights[l] < heights[r]:
                minheight = heights[l]
                l += 1
            else:

                minheight = heights[r]
                r -= 1
         
            maxArea = max(maxArea, minheight * width)
            
        return maxArea

        