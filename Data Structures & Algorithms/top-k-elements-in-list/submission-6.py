class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    

        count = Counter(nums)

        res = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        return res[:k]