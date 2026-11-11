class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in strsMap:
                strsMap[sortedS].append(s)
            else:
                strsMap[sortedS] = [s]

        res = [] 
        for key, val in strsMap.items():
            res.append(val)
        
        return res