class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        start = 0
        count = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_index = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]
                current = next_index
                count += 1
                if start == current:
                    break
            start += 1