class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        target = Counter(t)
        window = Counter()

        have = 0
        need = len(target)

        res = ""
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in target and window[c] == target[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]

                left_char = s[l]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1

                l += 1

        return res