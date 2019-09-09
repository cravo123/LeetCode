import collections
# Solution 1, use stack to record previous time-consumed
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        q = [[-1, 0]]
        prev_t = 0
        
        d = collections.Counter()
        
        for log in logs:
            f_id, flag, t = log.split(':')
            f_id = int(f_id)
            t = int(t)
            
            if flag == 'start':
                q[-1][1] += t - prev_t
                prev_t = t
                q.append([f_id, 0])
            else:
                q[-1][1] += t - prev_t + 1
                f_id, t_all = q.pop()
                d[f_id] += t_all
                prev_t = t + 1
        
        res = [d[i] for i in range(n)]
        
        return res