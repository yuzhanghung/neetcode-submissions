class Solution:
    def maxScore(self, s: str) -> int:
        left, right = "", ""
        score = 0

        for i in range(len(s) - 1):
            left = s[:i+1]
            right = s[i+1:]
            lenLeft = 0
            lenRight = 0

            for val in left:
                if val == "0":
                    lenLeft += 1

            for val in right:
                if val == "1":
                    lenRight += 1

            score = max(score, lenLeft + lenRight)

        return score
