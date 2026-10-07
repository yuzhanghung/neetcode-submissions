class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        group = {i:[] for i in range(1, n+1)}
        
        for u, v, t in times:
            group[u].append([v, t])
        
        minHeap = [(0, k)]

        path = {}

        while minHeap:
            cost, source = heapq.heappop(minHeap)

            if source in path:
                continue
            
            path[source] = cost

            for dest, edge_cost in group[source]:
                new_cost = cost + edge_cost
                heapq.heappush(minHeap, (new_cost, dest))
        

        if len(path) != n:
            return -1
        
        return max(path.values())