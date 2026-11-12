class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        bubble = [[] for i in range(len(nums) + 1)]

        for key, val in freq_map.items():
            bubble[val].append(key)

        res = []
        for i in range(len(bubble) - 1, 0, -1):
            for num in bubble[i]:
                res.append(num)
            if len(res) == k:
                return res