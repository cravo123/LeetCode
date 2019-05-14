import collections

# Solution 1, simulation
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        
        q_r = collections.deque()
        q_d = collections.deque()
        
        for i, c in enumerate(senate):
            if c == 'R':
                q_r.append(i)
            else:
                q_d.append(i)
        
        while q_r and q_d:
            i_r = q_r.popleft()
            i_d = q_d.popleft()
            
            if i_r < i_d:
                q_r.append(i_r + n)
            else:
                q_d.append(i_d + n)
        
        if q_r:
            return 'Radiant'
        return 'Dire'