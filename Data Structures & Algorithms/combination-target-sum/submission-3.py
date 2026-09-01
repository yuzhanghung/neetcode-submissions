class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, subset, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            if curSum > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, subset, curSum + nums[i])
            subset.pop()
            dfs(i + 1, subset, curSum)
        
        dfs(0, [], 0)
        return res