class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        shortest_path = float("inf")

        remainder = { 0 : -1 }
        curSum = 0
        prefixSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            r = curSum % p
            need = (r - target) % p
            if need in remainder:
                ealierIndex = remainder[need]
                length = i - ealierIndex
                shortest_path = min(shortest_path, length)

            remainder[r] = i
        
        return shortest_path if shortest_path < len(nums) else -1