import collections

# Solution 1, Topological Sorting
class Solution:
    def check(self, w1, w2, d):
        for a, b in zip(w1, w2):
            if a != b:
                d[b].add(a) # a < b
                return
    
    def alienOrder(self, words: List[str]) -> str:
        d = {}
        
        for word in words:
            for c in word:
                d[c] = set()
        
        total = len(d)
        n = len(words)
        
        for i in range(n - 1):
            prev, curr = words[i], words[i + 1]    
            self.check(prev, curr, d)                
        q = []
        
        for c in d:
            if len(d[c]) == 0:
                q.append(c)
        for c in q:
            del d[c]
        
        seen = q[::]
        
        while q:
            tmp = []
            
            # actually traversing dict and delete is expensive
            # could use indegree # to improve efficiency
            for c in d:
                for x in q:
                    d[c].discard(x)
                if len(d[c]) == 0:
                    tmp.append(c)
            
            seen.extend(tmp)
            for c in tmp:
                del d[c]
            q = tmp
        
        return ''.join(seen) if len(seen) == total else ''

# Solution 1.1 same idea but use indegree to track 
class Solution:
    def check_order(self, w1, w2, d, indegree):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c1 not in d[c2]:
                    d[c2].add(c1)
                    indegree[c2] += 1
                return
        
    def alienOrder(self, words: List[str]) -> str:
        indegree = collections.Counter()
        for word in words:
            for c in word:
                indegree[c] = 0
        
        d = collections.defaultdict(set)
        
        for prev, curr in zip(words, words[1:]):
            self.check_order(prev, curr, d, indegree)
        q = collections.deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
                indegree[c] -= 1
        
        res = []
        while q:
            x = q.popleft()
            res.append(x)
            for c in d:
                if x in d[c]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)
        return ''.join(res) if len(res) == len(indegree) else ''
                