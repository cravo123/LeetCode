import collections

# Solution 1, DFS
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = collections.defaultdict(set) # connected nodes
        path = set() # (a, b) will be in path if there is a path from a to b
        
        for a, b in connections:
            neighbors[b].add(a)
            neighbors[a].add(b)
            path.add((a, b))
        
        res = 0
        q = [0]
        seen = set(q)
        
        while q:
            curr = q.pop()
            for child in neighbors[curr]:
                if child not in seen:
                    seen.add(child)
                    q.append(child)
                    if (child, curr) not in path:
                        res += 1
        
        return res