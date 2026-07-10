class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        seen = {
            0 : 1
        }
        res = 0

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in seen:
                res += seen[prefix - k]
            
            seen[prefix] = seen.get(prefix, 0) + 1

        return res