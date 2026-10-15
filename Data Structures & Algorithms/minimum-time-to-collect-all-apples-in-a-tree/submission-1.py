class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {} # node : neighbor
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)


        def dfs(cur, par):
            time = 0

            for child in adj[cur]:
                if child == par:
                    continue
                childTime = dfs(child, cur)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            
            return time
        
        return dfs(0, -1)
            
            
        