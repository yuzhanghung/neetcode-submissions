class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            seen = set()

            for i in range(len(nums)):
                if i in used:
                    continue
                
                if nums[i] in seen:
                    continue

                used.add(i)
                seen.add(nums[i])
                subset.append(nums[i])
            
                dfs(subset)
                subset.pop()
                used.remove(i)
        
        dfs([])
        return res
