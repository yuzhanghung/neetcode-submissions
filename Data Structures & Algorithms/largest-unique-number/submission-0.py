class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_uniq = -1

        cnt = Counter(nums)

        for key, val in cnt.items():
            if val == 1:
                max_uniq = max(max_uniq, key)
        
        return max_uniq
        