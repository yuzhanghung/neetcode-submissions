class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            root_n1 = find(n1)
            root_n2 = find(n2)
            if root_n1 != root_n2:
                if rank[root_n1] < rank[root_n2]:
                    par[root_n1] = root_n2
                    rank[root_n2] += rank[root_n1]
                else:
                    par[root_n2] = root_n1
                    rank[root_n1] += rank[root_n2]
                return True
            return False
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        
