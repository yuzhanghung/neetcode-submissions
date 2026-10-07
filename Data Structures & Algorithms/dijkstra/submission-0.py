class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # node: val
        # minheap

        group = {i: [] for i in range(n)}

        for source, dst, cst in edges:
            group[source].append([dst, cst])
                

        minHeap = [(0, src)]

        path = {}

        while minHeap:
            cost, source = heapq.heappop(minHeap)
            
            if source in path:
                continue 

            path[source] = cost

            for dest, edgeCost in group[source]:
                newCost = cost + edgeCost
                heapq.heappush(minHeap, (newCost, dest))
        
        for node in range(n):
            if node not in path:
                path[node] = -1
            
        return path


        