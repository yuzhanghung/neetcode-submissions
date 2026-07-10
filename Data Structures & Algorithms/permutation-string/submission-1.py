class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        window = Counter(s1)

        l = 0

        for r in range(len(s2) - length + 1):
            chars = s2[r:r+length]
            if window == Counter(chars):
                return True
            
        return False
