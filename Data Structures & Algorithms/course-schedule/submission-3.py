class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

        visiting = set()
        visited = set()
        

        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False
            
            visiting.add(src)
            for n in adj[src]:
                if not dfs(n):
                    return False
            visiting.remove(src)
            visited.add(src)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        