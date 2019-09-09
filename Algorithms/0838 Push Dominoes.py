# By Chong Chen, https://github.com/cravo123/LeetCode

import collections

# Solution 1, adjacent symbols
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        symbols = [[i, c] for i, c in enumerate(dominoes) if c != '.']
        symbols = [[-1, 'L']] + symbols + [[len(dominoes), 'R']]
        
        for (i, c1), (j, c2) in zip(symbols, symbols[1:]):
            if c1 == c2:
                for k in range(i + 1, j):
                    dominoes[k] = c1
            elif c1 == 'L' and c2 == 'R':
                continue
            else:
                left, right = i + 1, j - 1
                
                while left <= right:
                    if left == right:
                        left += 1
                        right -= 1
                    else:
                        dominoes[left] = c1
                        dominoes[right] = c2
                        left += 1
                        right -= 1
        return ''.join(dominoes)


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
                    
                