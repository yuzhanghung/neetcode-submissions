class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        sub = Counter()
        l = 0
        res = ""
        required = len(target)
        formed = 0

        for r in range(len(s)):
            char = s[r]
            if char in target:
                sub[char] += 1
                if sub[char] == target[char]:
                    formed += 1

            while formed == required:
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r + 1]

                left_char = s[l]
                if left_char in target:
                    if sub[left_char] == target[left_char]:
                        formed -= 1
                    sub[left_char] -= 1

                l += 1

        return res