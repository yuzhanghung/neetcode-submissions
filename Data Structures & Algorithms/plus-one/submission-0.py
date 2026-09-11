class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        length = len(digits)

        for digit in digits:
            num = num * 10 + digit

        num += 1
        res = []

        while num != 0:
            res.append(num % 10)
            num //= 10

        return res[::-1]