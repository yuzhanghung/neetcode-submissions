class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        pers = [[]]

        for num in nums:
            new_pers = []
            
            for p in pers:
                for i in range(len(p) + 1):
                    p_copy = list(p)
                    p_copy.insert(i, num)
                    if p_copy not in new_pers:
                        new_pers.append(p_copy)
            
            pers = new_pers
        return pers
        