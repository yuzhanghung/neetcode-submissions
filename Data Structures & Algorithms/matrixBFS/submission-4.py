class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROW-1][COLS-1] == 1:
            return -1

        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))
        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COLS - 1:
                    return length

                neighbor = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in neighbor:
                    new_r, new_c = r + dr, c + dc
                    if (min(new_r, new_c) < 0 
                    or new_r == ROW 
                    or new_c == COLS 
                    or (new_r, new_c) in visited 
                    or grid[new_r][new_c] == 1):
                        continue
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

            length += 1
        return -1