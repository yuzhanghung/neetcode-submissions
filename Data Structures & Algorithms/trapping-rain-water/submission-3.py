class Solution:
    def trap(self, height: List[int]) -> int:
        maxRight = [0] * len(height)
        maxR = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = maxR
            maxR = max(maxR, height[i])
        #print(maxRight)

        res = 0
        maxL = 0
        for i in range(len(height)):
            water = min(maxL, maxRight[i]) - height[i] 
            trapped_water = water if water > 0 else 0
            res += trapped_water
            maxL = max(maxL, height[i])
        return res
            

