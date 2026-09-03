class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visit = set()
        res = 0
        val = 0


        def dfs(r, c):
            if (min(r, c) < 0 or
                r == rows or c == cols or
                (r, c) in visit or 
                grid[r][c] == 0):
                return 0

            visit.add((r, c))
         
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                val = dfs(r, c)
                res = max(res, val)
        return res