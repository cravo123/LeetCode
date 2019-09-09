import collections

# Solution 1, topological sorting
# Maintain out_degree count, and node to parent_node dict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = {}
        d = collections.defaultdict(list) # curr -> parent
        
        for i, v in enumerate(graph):
            out_degree[i] = len(v)
            for j in v:
                d[j].append(i)
        
        res = []
        curr = [i for i in range(n) if out_degree[i] == 0]
        
        while curr:
            res.extend(curr)
            
            tmp = []
            
            for i in curr:
                for j in d[i]:
                    out_degree[j] -= 1
                    if out_degree[j] == 0:
                        tmp.append(j)
            curr = tmp
        res.sort()
        
        return res

# Solution 2, find circle in a graph
# white-gray-black algorithm
# t.b.c