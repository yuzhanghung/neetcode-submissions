class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_map = Counter(s1)
        s2_map = {}

        for r in range(len(s2)):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            if r - l + 1 == len(s1):
                if s2_map == s1_map:
                    return True
                else:
                    s2_map[s2[l]] -= 1
                    if s2_map[s2[l]] == 0:
                        del s2_map[s2[l]]
                    l += 1
        
        return False
