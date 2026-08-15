class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COLS = len(grid), len(grid[0])

        def helper(r, c, visited):
            if (min(r, c) < 0 
            or r == ROW or c == COLS 
            or grid[r][c] == 1 
            or (r, c) in visited): return 0

            if r == ROW - 1 and c == COLS - 1:
                return 1
            
            visited.add((r, c))

            count = 0
            count += helper(r + 1, c, visited)
            count += helper(r - 1, c, visited)
            count += helper(r, c + 1, visited)
            count += helper(r, c - 1, visited)

            visited.remove((r, c))
            return count

        return helper(0, 0, set())

