class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isdigit():
                subLen = ""
                while j < len(abbr) and abbr[j].isdigit():
                    subLen += abbr[j]
                    j += 1
                i += int(subLen)
            else:
                return False
        
        return i == len(word) and j == len(abbr)
