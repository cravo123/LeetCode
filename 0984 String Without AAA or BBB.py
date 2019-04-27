import heapq

# Solution 1, greedy
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        cnt1, c1 = A, 'a'
        cnt2, c2 = B, 'b'
        
        if cnt1 < cnt2:
            cnt1, cnt2 = cnt2, cnt1
            c1, c2 = c2, c1
        
        q = []
        
        while cnt1 > 0 and cnt2 > 0:
            if cnt1 > cnt2:
                v1, v2 = 2, 1
            elif cnt1 < cnt2:
                v1, v2 = 1, 2
            else:
                v1 = v2 = 1
                
            q.append(c1 * v1)
            q.append(c2 * v2)
            cnt1 -= v1
            cnt2 -= v2
        
        
        if cnt1 > 0:
            q.append(c1 * cnt1)
        if cnt2 > 0:
            q.append(c2 * cnt2)
        q = ''.join(q)
        
        return q

# Solution 2, priority queue, similar to 
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        q = []
        if A > 0:
            q.append([-A, 'a'])
        if B > 0:
            q.append([-B, 'b'])
        
        heapq.heapify(q)
        
        res = []
        
        while q:
            cnt1, c1 = heapq.heappop(q)
            if not q:
                res.append(c1 * abs(cnt1))
                break
            cnt2, c2 = heapq.heappop(q)
            
            if cnt1 < cnt2:
                res.append(c1)
                cnt1 += 1
            res.append(c1)
            res.append(c2)
            cnt1 += 1
            cnt2 += 1
            
            if cnt1 < 0:
                heapq.heappush(q, [cnt1, c1])
            
            if cnt2 < 0:
                heapq.heappush(q, [cnt2, c2])
        
        res = ''.join(res)
        
        return res
                