class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        island = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [
                    [row + 1, col],
                    [row - 1, col],
                    [row, col + 1],
                    [row, col - 1]
                ]

                for nr, nc in directions:
                    if (
                        min(nr, nc) < 0 or 
                        nr >= rows or 
                        nc >= cols or 
                        grid[nr][nc] == "0"
                    ):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = "0"




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1

        return island