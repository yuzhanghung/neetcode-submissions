class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        island = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            area = 1
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
                        nr >= ROWS or
                        nc >= COLS or
                        grid[nr][nc] == 0
                    ):
                        continue
                    area += 1
                    grid[nr][nc] = 0
                    q.append((nr, nc))

            return area



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    island = max(island, area)


        return island