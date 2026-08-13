class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        i = 1

        while i < k:
            heapq.heappop(nums)
            i += 1

        val = heapq.heappop(nums)

        return -val