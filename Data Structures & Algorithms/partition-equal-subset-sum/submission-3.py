class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for t in range(target, n - 1, -1):
                if dp[t - n]:
                    dp[t] = True

        return dp[target]