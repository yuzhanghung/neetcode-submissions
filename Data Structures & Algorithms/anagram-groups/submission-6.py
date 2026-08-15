class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = # of strings 
        # k = max length of a string
        # the time complexity = O (n * k log k)
        # the space complexity = O (n * k)
        res = {}

        for s in strs: # n 
            sortedS = "".join(sorted(s)) # k long k 
            if sortedS in res:
                res[sortedS].append(s)
            else:
                res[sortedS] = [s]
        
        return list(res.values())

