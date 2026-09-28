class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums)

        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            self.prefixSum[i] = prefix

    def sumRange(self, left: int, right: int) -> int:
        leftVal = self.prefixSum[left - 1] if left > 0 else 0
        return self.prefixSum[right] - leftVal
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)