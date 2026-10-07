class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        group = {i:[] for i in range(n)}

        for u, v, w in edges:
            group[u].append((v, w))
            group[v].append((u, w))

        minHeap = [(0, 0)]
        res = 0
        

        while minHeap and len(visit) < n:
            w, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            
            res += w
            visit.add(u)

            for v, w in group[u]:
                if v not in visit:
                    
                    heapq.heappush(minHeap, (w, v))


        return res if len(visit) == n else -1