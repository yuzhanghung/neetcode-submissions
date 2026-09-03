class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        
        q = deque()
        visit = set()
        q.append((0, 0))
        visit.add((0, 0))

        length = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for dr, dc in neighbors:
                    if (min(dr, dc) < 0 or
                        dr == ROWS or 
                        dc == COLS or
                        (dr, dc) in visit or
                        grid[dr][dc] == 1):
                        continue
                    
                    q.append((dr, dc))
                    visit.add((dr, dc))
            length += 1
        
        return -1
