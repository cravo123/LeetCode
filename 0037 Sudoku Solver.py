class Solution:
    def eligible(self, i, j, board):
        seen = set(board[i])
        
        for x in range(9):
            seen.add(board[x][j])
        
        i, j = i // 3 * 3, j // 3 * 3
        
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                seen.add(board[x][y])
        
        for c in range(1, 10):
            c = str(c)
            if c not in seen:
                yield c
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in self.eligible(i, j, board):
                        board[i][j] = c
                        if self.solve(board):
                            return True
                    board[i][j] = '.'
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)