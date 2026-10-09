class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_i] = root_j
            self.rank[root_j] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = []

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj.append([i, j, dist])
                adj.append([j, i, dist])

        minHeap = []
        for n1, n2, dist in adj:
            heapq.heappush(minHeap, [dist, n1, n2])

        unionFind = UnionFind(N)
        res = 0
        mst = []

        while len(mst) < N - 1:
            dist, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            res += dist
            mst.append([n1, n2])
        return res