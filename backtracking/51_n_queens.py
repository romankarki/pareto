from typing import List

class Solution: 

    def solve_n_queens(self, n: int ) -> List[List[str]]:
        
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(0, n):
                if self.check_safe(r,c, board):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."

        backtrack(0)
        return res 
    
    def check_safe(self, r: int, c: int, board: List[List[str]]) -> bool:

        row = r - 1
        #check vertically above ||
        while row >= 0:
            if board[row][c] == "Q":
                return False 
            row -= 1
        
        #check Diagonal \\
        row, col = r-1, c-1
        while row >=0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        #check Diagonal //
        row, col = r -1, c + 1
        while row >= 0 and col < len(board[0]):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        return True
    


