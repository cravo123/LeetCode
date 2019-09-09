import collections

# Solution 1, topological sorting
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        parents = collections.defaultdict(set)
        children = collections.defaultdict(set)
        
        node = set()
        
        for seq in seqs:
            n = len(seq)
            for i in range(n):
                node.add(seq[i])
                if i < n - 1:
                    children[seq[i]].add(seq[i + 1])
                if i > 0:
                    parents[seq[i]].add(seq[i - 1])
        
        curr = [i for i in node if not parents[i]]
        res = []
        
        while len(curr) == 1:
            x = curr.pop()
            res.append(x)
            node.discard(x)
            
            for p in children[x]:
                parents[p].discard(x)
                if not parents[p]:
                    curr.append(p)
                
        return res == org and not node

# Solution 1.1,
# Topological sorting template
# Use indegree to mark count of parents, and children to cache children nodes
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        indegree = collections.Counter()
        children = collections.defaultdict(set)
        
        for seq in seqs:
            n = len(seq)
            for i in range(n):
                if seq[i] not in indegree:
                    indegree[seq[i]] = 0
                if i < n - 1 and seq[i + 1] not in children[seq[i]]:
                    indegree[seq[i + 1]] += 1
                    children[seq[i]].add(seq[i + 1])
        
        curr = []
        for i in indegree:
            if indegree[i] == 0:
                curr.append(i)
        
        res = []
        
        while curr:
            if len(curr) > 1:
                return False
            x = curr.pop()
            indegree[x] -= 1
            res.append(x)
            for p in children[x]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    curr.append(p)
        return org == res and all(indegree[x] < 0 for x in indegree)

# Solution 2, toplogical sorting, TLE
# The reason why it gets TLE is because there is a test with too many numbers
# so loop through dict is expensive
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        d = collections.defaultdict(set) # child -> parents
        cans = set(x for seq in seqs for x in seq)
        for seq in seqs:
            for a, b in zip(seq, seq[1:]):
                d[b].add(a)
        
        res = []
        n = len(org)
        curr = [i for i in cans if len(d[i]) == 0]
        seen = set(curr)
        
        while curr:
            if len(curr) > 1:
                return False
            x = curr.pop()
            res.append(x)
            
            for i in d: # this step is expensive
                if i not in seen:
                    d[i].discard(x)
                    if not d[i]:
                        curr.append(i)
                        seen.add(i)
            
        return res == org