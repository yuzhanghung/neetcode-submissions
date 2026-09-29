class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            qLen = len(q)

            for _ in range(qLen):
                r, c = q.popleft()
                dic = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]
                for nr, nc in dic:
                    if (
                        min(nr, nc) < 0 or
                        nr == rows or nc == cols
                    ):
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1
                