class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] or grid[rows - 1][cols - 1]:
            return -1

        q = deque()
        q.append((0, 0))
        visit = set()
        visit.add((0, 0))

        length = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                neighbors = [
                    [r + 1, c], 
                    [r - 1, c], 
                    [r, c + 1], 
                    [r, c - 1],
                    [r + 1, c + 1],
                    [r + 1, c - 1],
                    [r - 1, c + 1],
                    [r - 1, c - 1]]
                    
                for nr, nc in neighbors:
                    if (min(nr, nc) < 0 or
                        nr == rows or nc == cols or
                        (nr, nc) in visit or 
                        grid[nr][nc] == 1):
                        continue
                    
                    q.append((nr, nc))
                    visit.add((nr, nc))

            length += 1

        return -1
            