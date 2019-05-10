# By Chong Chen, https://github.com/cravo123/LeetCode

import collections

# Solution 1, 



# Solution 2, BFS simulation
# At each step we maintain the index that will change in the next step
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        
        curr = [i for i in range(n) if dominoes[i] != '.']
        seen = set(curr)
        
        while curr:
            tmp = collections.defaultdict(set)
            
            for i in curr:
                if dominoes[i] == 'L':
                    if i > 0 and dominoes[i - 1] == '.' and i - 1 not in seen:
                        tmp[i - 1].add('L')
                else:
                    if i < n - 1 and dominoes[i + 1] == '.' and i + 1 not in seen:
                        tmp[i + 1].add('R')
            
            q = []
            
            for i in tmp:
                seen.add(i)
                if len(tmp[i]) == 2:
                    continue
                dominoes[i] = tmp[i].pop()
                q.append(i)
            curr = q
        
        res = ''.join(dominoes)
        
        return res
                    
                