import collections
# Solution 1, back-tracking with pruning.
# Prune by sorting
class Solution:
    def dfs(self, path, d, total):
        if len(path) == total + 1:
            self.res = path[::]
            return True
        
        curr = path[-1]
        for next_pt in sorted(d[curr]):
            if d[curr][next_pt] > 0:
                path.append(next_pt)
                d[curr][next_pt] -= 1
                if self.dfs(path, d, total):
                    return True
                d[curr][next_pt] += 1
                path.pop()
        return False
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(collections.Counter)
        
        total = 0
        for start, end in tickets:
            d[start][end] += 1
            total += 1
        
        self.res = None
        path = ['JFK']
        
        self.dfs(path, d, total)
        
        return self.res

# Solution 1.1, back-tracking (TLE)
class Solution:
    def dfs(self, path, res, d, cnt, total):
        if len(path) == total + 1:
            if not res:
                res.append(path[::])
            else:
                for i in range(len(path)):
                    if path[i] < res[0][i]:
                        res[0] = path[::]
                        break
                    elif path[i] > res[0][i]:
                        break
            return
        
        curr = path[-1]
        for next_point in d[curr]:
            if cnt[curr, next_point] > 0:
                path.append(next_point)
                cnt[curr, next_point] -= 1
                self.dfs(path, res, d, cnt, total)
                cnt[curr, next_point] += 1
                path.pop()
            
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(set)
        cnt = collections.Counter()
        total = 0
        for start, end in tickets:
            d[start].add(end)
            cnt[start, end] += 1
            total += 1
        
        res = []
        path = ['JFK']
        
        self.dfs(path, res, d, cnt, total)
        
        return res[0]

# Solution 2, Eulerian Path, Hierholzer's algorithm
# t.b.c
        