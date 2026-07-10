class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        window = Counter(s1)

        for i in range(len(s2) - length + 1):
            chars = s2[i:i+length]
            if window == Counter(chars):
                return True
            
        return False
