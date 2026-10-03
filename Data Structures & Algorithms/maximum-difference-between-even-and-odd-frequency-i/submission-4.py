class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd, even = 0, float("inf")


        for val in cnt.values():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)

        return odd - even