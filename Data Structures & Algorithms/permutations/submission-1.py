class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for num in nums:
                if num in used:
                    continue
                subset.append(num)
                used.add(num)
                dfs(subset)
                subset.pop()
                used.remove(num)
        dfs([])
        return res
