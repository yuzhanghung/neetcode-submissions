class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(val: int):
            sqrSum = 0
            while val:
                sqr = (val % 10) ** 2
                sqrSum += sqr
                val = val // 10
            return sqrSum
        
        
        seen = set()


        while n:
            n = sqr(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)


        