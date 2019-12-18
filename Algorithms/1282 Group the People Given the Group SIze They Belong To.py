import collections

# Solution 1, simulation
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.Counter(groupSizes)
        
        q = collections.defaultdict(list)
        
        for i, v in enumerate(groupSizes):
            q[v].append(i)
        
        res = []
        
        for sz, vs in q.items():
            for i in range(0, len(vs), sz):
                res.append(vs[i:(i + sz)])
        
        return res