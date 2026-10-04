class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1

            if len(cnt) <= 2:
                continue
            
            new_dict = defaultdict(int)
            for key, val in cnt.items():
                if val > 1:
                    new_dict[key] = val - 1
            cnt = new_dict

        
        res = []
        for key, val in cnt.items():
            if nums.count(key) > len(nums) / 3:
                res.append(key)
        
        return res
        