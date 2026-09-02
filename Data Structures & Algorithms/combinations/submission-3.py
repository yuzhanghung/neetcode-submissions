class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        res = []

        def dfs(subset, i, j):
            if j == k:
                res.append(subset.copy())
                return
            if i == len(nums):
                return 
            subset.append(nums[i])
            dfs(subset, i + 1, j + 1)
            subset.pop()
            dfs(subset, i + 1, j)

        dfs([], 0, 0)
        return res
