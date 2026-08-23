class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = sum(range(n + +1))
        actual = sum(nums)

        return expected - actual