class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        
        cache = [[0] * cols for _ in range(rows)]

        def top_bottom(r, c):
            if r == rows or c == cols:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = top_bottom(r + 1, c) + top_bottom(r, c + 1)
            return cache[r][c]
        
        return top_bottom(0, 0)