class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # {0:1}, if index 0 is k
        # needed = curSum - k
        # if needed in dict, if so, we are adding the count to res
        # otherwise, we will record 
        # different occurance of number represent different valid subarrays

        prefixSum = {0: 1}
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            needed = curSum - k
            if needed in prefixSum:
                res += prefixSum[needed]
            if curSum in prefixSum:
                prefixSum[curSum] += 1
            else:
                prefixSum[curSum] = 1
        
        return res