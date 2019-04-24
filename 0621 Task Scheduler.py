import collections

# Solution 1, Math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        d = collections.Counter(tasks)
        v = d.most_common(1)[0][1]
        
        cnt = 0
        for c in d:
            if d[c] == v:
                cnt += 1
        # (v - 1) filling blocks each with width of n
        # we already filled (n - cnt + 1) for each block
        return len(tasks) + max(0, (n - cnt + 1) * (v - 1) - len(tasks) + cnt * v) 

# Solution 2 priority queue
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = collections.Counter(tasks)
        q = [-v for v in d.values()]
        heapq.heapify(q)
        
        res = 0
        while q:
            tmp = []
            
            for _ in range(n + 1):
                if q:
                    x = heapq.heappop(q)
                    x += 1
                    if x != 0:
                        tmp.append(x)
                res += 1
                
                if len(q) == 0 and len(tmp) == 0:
                    return res
            for x in tmp:
                heapq.heappush(q, x)
        return res
            