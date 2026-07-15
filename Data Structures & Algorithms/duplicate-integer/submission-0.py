class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

        return False