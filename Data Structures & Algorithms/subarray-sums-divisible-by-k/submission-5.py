class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        remainder = { 0 : 1 }

        curSum = 0
        for num in nums:
            curSum += num
        
            r = curSum % k
            if r in remainder:
                res += remainder[r]
                
            
            remainder[r] = remainder.get(r, 0) + 1
        
        return res

