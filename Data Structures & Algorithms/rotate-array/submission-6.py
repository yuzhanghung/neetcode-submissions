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
            cur_index = start
            temp = nums[start]
            while True:
                next_index = (cur_index + k) % n
                nums[next_index], temp = temp, nums[next_index]
                cur_index = next_index
                count += 1
                if cur_index == start:
                    break
            start += 1

