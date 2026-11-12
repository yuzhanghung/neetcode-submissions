class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        bubble = [[] for i in range(len(nums) + 1)]

        for key, val in freq_map.items():
            bubble[val].append(key)

        res = []
        for i in range(len(bubble) - 1, - 1, -1):
            if bubble[i]:
                res.extend(bubble[i])
                k -= len(bubble[i])
                if k == 0:
                    return res