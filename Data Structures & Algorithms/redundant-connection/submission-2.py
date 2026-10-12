class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        size = [1] * (n + 1)
        parent = [i for i in range(n + 1)]

        def union(n1, n2):
            root_n1 = find(n1)
            root_n2 = find(n2)
            if root_n1 != root_n2:
                if size[root_n1] < size[root_n2]:
                    parent[root_n1] = root_n2
                    size[root_n2] += size[root_n1]
                else:
                    parent[root_n2] = root_n1
                    size[root_n1] += size[root_n2]

                return True
            return False
            
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        