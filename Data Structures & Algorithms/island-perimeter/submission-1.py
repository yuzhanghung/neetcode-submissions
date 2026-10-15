class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))
                    break
            if q:
                break

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]  

        while q:            
            r, c = q.popleft()
            
            if (min(r, c) < 0 or
                r == rows or
                c == cols or
                grid[r][c] == 0 or
                (r, c) in visit
                ):
                    continue

            visit.add((r, c)) 
            

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or
                    nc < 0 or
                    nr >= rows or
                    nc >= cols or
                    grid[nr][nc] == 0
                    ):
                        res += 1
                elif (nr, nc) not in visit:
                    q.append((nr, nc))

                
        return res

        
        
        