class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # elemnt: count

        for num in nums: #O(n)
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # cnt: element
        bucket = [[] for i in range(len(nums) + 1)]


        for key, val in freq.items():
            bucket[val].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res


            

