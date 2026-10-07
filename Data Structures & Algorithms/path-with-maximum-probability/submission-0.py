class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        group = {i:[] for i in range(n)}

        for i in range(len(edges)):
            src, dst = edges[i]
            prob = succProb[i]

            group[src].append((dst, prob))
            group[dst].append((src, prob))
        
        maxHeap = [(-1.0, start_node)]
        path = {}

        while maxHeap:
            neg_prob, src = heapq.heappop(maxHeap)

            prob = -neg_prob

            if src in path: 
                continue
            
            path[src] = prob

            if src == end_node:
                return prob

            for dst, probability in group[src]:
                new_prob = prob * probability
                heapq.heappush(maxHeap, (-new_prob, dst))

        return 0
