class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c, visit, pixel):
            if (min(r, c) < 0 or 
                r == ROWS or c == COLS or
                image[r][c] != pixel or 
                (r, c) in visit):
                return

            pixel = image[r][c]
            image[r][c] = color
            visit.add((r, c))
            dfs(r + 1, c, visit, pixel)
            dfs(r - 1, c, visit, pixel)
            dfs(r, c + 1, visit, pixel)
            dfs(r, c - 1, visit, pixel)
            
        dfs(sr, sc, set(), image[sr][sc])
        return image
