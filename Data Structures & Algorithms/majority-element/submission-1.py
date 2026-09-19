class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}

        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1

        
            
        for key, val in cnt.items():
            if val > (len(nums) / 2):
                return key

