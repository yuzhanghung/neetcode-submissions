class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)

        res = []

        for key, val in cnt.items():
            if val > len(nums) / 3:
                res.append(key)

        return res