class UnionFind:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToIndex = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToIndex:
                    uf.union(i, emailToIndex[e])
                else:
                    emailToIndex[e] = i
        
        groupEmail = defaultdict(list)
        for e, i in emailToIndex.items():
            leader = uf.find(i)
            groupEmail[leader].append(e)

        res = []
        for i, emails in groupEmail.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        
        return res
