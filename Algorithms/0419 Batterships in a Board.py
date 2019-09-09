# Solution 1, simulation
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        
        m, n = len(board), len(board[0]) if board else 0
        
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'X' 
                    and (i == 0 or board[i - 1][j] == '.') 
                    and (j == 0 or board[i][j - 1] == '.')):
                    res += 1
        
        return res