class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in val:
                return [val[diff], i]
            val[nums[i]] = i