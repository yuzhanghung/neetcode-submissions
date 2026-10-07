class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        res = nums[0]

        for n in nums[1:]:
            tmp = max_product
            max_product = max(tmp * n, min_product * n, n)
            min_product = min(n, tmp * n, min_product * n)
            res = max(res, max_product)

        return res