class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        count = {}
        max_f = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            
            if r - l + 1 - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res