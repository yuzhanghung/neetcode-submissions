class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in res:
                res[sortedS].append(s)
            else:
                res[sortedS] = [s]
        
        return list(res.values())