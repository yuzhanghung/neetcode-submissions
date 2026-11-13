class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            k = i
            while s[i] != "#":
                i += 1

            length = s[k : i]
            string = s[i + 1 : i + 1 + int(length)]
            res.append(string)
            i = i + 1 + int(length)
        
        return res
                    
