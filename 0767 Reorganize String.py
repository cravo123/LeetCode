import collections
import heapq
# Similar as LC 0621

# Solution 1,
# Assume most common value is c and its frequency is v, then we have,
# c__c__c...__c
# so we need to fill at least (v - 1) slots, otherwise we cannot make two adjacent
# chars different, so if total length is n, then we have (n - v) chars needs to fill 
# v - 1 holes, => n - v >= v - 1
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        
        n = len(S)
        d = collections.Counter(S)
        c, v = d.most_common(1)[0]
        
        if 2 * v - n - 1 > 0:
            return ''
        
        res = [[c] for _ in range(v)]
        res.append([])
        
        idx = 0
        for x in sorted(d, key=lambda x: -d[x]):
            if x != c:
                for _ in range(d[x]):
                    res[idx].append(x)
                    idx = (idx + 1) % (v + 1)
        
        res = ''.join(''.join(x) for x in res)
        
        return res

# Solution 2, priority queue solution, more elegant
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = collections.Counter(S)
        
        q = [[-v, c] for c, v in d.items()]
        
        heapq.heapify(q)
        res = []
        while len(q) > 1:
            v1, c1 = heapq.heappop(q)
            v2, c2 = heapq.heappop(q)
            
            res.append(c1)
            res.append(c2)
            
            v1 += 1
            v2 += 1
            
            if v1 != 0:
                heapq.heappush(q, [v1, c1])
            if v2 != 0:    
                heapq.heappush(q, [v2, c2])
        
        if len(q) == 1 and q[0][0] < -1:
            return ''
        if len(q) == 1:
            res.append(q[0][1])
        
        res = ''.join(res)
        
        return res