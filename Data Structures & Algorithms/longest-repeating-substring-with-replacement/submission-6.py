class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxF = 0
        res = 0

        for r in range(len(s)):
            window = r - l + 1
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxF = max(maxF, freq[s[r]])
            if window - maxF > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res

            
                
        


