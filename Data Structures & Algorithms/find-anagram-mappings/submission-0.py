class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        mapping = {} # val : index

        for i, n in enumerate(nums2):
            mapping[n] = i
        
        for n in nums1:
            if n in mapping:
                res.append(mapping[n])

        return res

        