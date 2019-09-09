# Solution 1, simulation
class Solution:
    def count(self, tag, board):
        res = sum(row.count(tag) for row in board)
        return res
    
    def has_win(self, tag, board):
        # Horizontal
        if any(row == tag * 3 for row in board):
            return True
        
        # Vertical
        if any(all(row[j] == tag for row in board) for j in range(3)):
            return True
        
        # diagonal
        if all(board[i][i] == tag for i in range(3)):
            return True
        
        # Anti-diagonal
        if all(board[i][2 - i] == tag for i in range(3)):
            return True
        
        return False
        
    def validTicTacToe(self, board: List[str]) -> bool:
        x_cnt, o_cnt = self.count('X', board), self.count('O', board)
        x_win, o_win = self.has_win('X', board), self.has_win('O', board)
        
        if o_cnt > x_cnt or x_cnt > o_cnt + 1:
            return False
        
        if o_win and x_cnt > o_cnt:
            return False
        
        if x_win and x_cnt == o_cnt:
            return False
        
        return True
        
        
        