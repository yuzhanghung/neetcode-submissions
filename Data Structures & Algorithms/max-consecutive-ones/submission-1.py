class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        ones = 0

        for n in nums:
            if n == 1:
                ones += 1
            else:
                ones = 0
            
            res = max(res, ones)
        
        return res