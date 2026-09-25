class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        i = n - 2

        while i >= 0:
            tmp = first
            first += second
            second = tmp
            i -= 1

        return first