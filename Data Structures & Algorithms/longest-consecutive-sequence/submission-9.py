class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                total = 1
                j = i
                while j + 1 in nums_set:
                    total += 1
                    j += 1
                res = max(res, total)
            else:
                continue
            
        
        return res