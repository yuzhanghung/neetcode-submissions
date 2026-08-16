class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        per = Counter()
        l = 0

        for r in range(len(s2)):
            per[s2[r]] += 1

            if (r - l + 1) > len(s1):
                per[s2[l]] -= 1

                if per[s2[l]] == 0:
                    del per[s2[l]] 
                
                l += 1
            
            if r - l + 1 == len(s1) and per == target:
                return True

        return False



        