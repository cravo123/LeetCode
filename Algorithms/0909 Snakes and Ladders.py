# Solution 1, BFS
# We first transform board to 1-D array to facilitate calculation
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0]) if board else 0
        
        dp = [0]
        
        flag = True
        for i in range(m - 1, -1, -1):
            if flag:
                for j in range(n):
                    dp.append(board[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    dp.append(board[i][j])
            flag = not flag
        
        dst = m * n
        steps = 0
        
        q = [1]
        seen = set(q)
        
        while q:
            tmp = []
            
            for x in q:
                if x == dst:
                    return steps
                for y in range(x + 1, min(x + 7, dst + 1)):
                    t = dp[y] if dp[y] != -1 else y
                    if t not in seen:
                        tmp.append(t)
                        seen.add(t)
            q = tmp
            steps += 1
        return -1

# Solution 2, BFS same idea but without transforming board to 1-D
# t.b.c