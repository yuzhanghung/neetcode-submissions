class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)

        for _ in range(k):
            for i in range(len(nums) - 1, 0, -1):
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
           


        