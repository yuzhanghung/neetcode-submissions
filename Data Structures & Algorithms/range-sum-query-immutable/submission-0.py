class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArray = []
        total = 0
        for num in nums:
            total += num
            self.sumArray.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        rightNum = self.sumArray[right]
        leftNum = self.sumArray[left - 1] if left > 0 else 0
        return (rightNum - leftNum)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)