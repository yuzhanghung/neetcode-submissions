class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        group = {i:[] for i in range(n)}

        for u, v, w in edges:
            group[u].append((v, w))
            group[v].append((u, w))

        minHeap = [(0, 0)] #weight, source
        res = 0
        path = set()

        while minHeap:
            weight, source = heapq.heappop(minHeap)

            if source in path:
                continue
            
            res += weight
            
            path.add(source)

            for dest, w in group[source]:
                if dest not in path:
                    heapq.heappush(minHeap, (w, dest))

        return res if len(path) == n else -1

        


        