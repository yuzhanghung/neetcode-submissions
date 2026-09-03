class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        res = 0
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or
                r == rows or c == cols or
                (r, c) in visit or 
                grid[r][c] == "0"):
                return 0
            
            

            visit.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return 1

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    res += 1
        
        return res

            

            