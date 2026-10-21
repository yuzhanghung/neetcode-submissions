class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        shortest_path = float("inf")

        for i in range(len(nums)):
            curSum = nums[i]
            if curSum % p == target:
                shortest_path = min(1, shortest_path)
            for j in range(i + 1, len(nums)):
                curSum += nums[j]
                if curSum % p == target:
                    shortest_path = min(j - i + 1, shortest_path)

        return shortest_path if shortest_path < len(nums) else -1