class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

 
        visited = set()
        

        def dfs(src):
            if src in visited:
                return False
            if adj[src] == []:
                return True
            
            visited.add(src)
            for n in adj[src]:
                if not dfs(n):
                    return False
            
            visited.remove(src)
            adj[src] = []
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        