class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        window = set()

        for num in nums:
            if num in window:
                return True
            window.add(num)

        return False