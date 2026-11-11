class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = {}

        for st in strs:
            count = [0] * 26
            for s in st:
                index = ord(s) - ord("a")
                count[index] += 1
            key = tuple(count)
            if key in strsMap:
                strsMap[key].append(st)
            else:
                strsMap[key] = [st]

        res = []
        for key, val in strsMap.items():
            res.append(val)

        return res
