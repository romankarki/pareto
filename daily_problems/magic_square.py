from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        for r in range(0, R-2):
            for c in range(0, C-2):
                # new_grid  = [
                #     [grid[r][c], grid[r][c+1], grid[r][c+2]],
                #     [grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]],
                #     [grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]]
                # ]
                new_grid = [row[c : c+3] for row in grid[r : r+3]]
               
                if self.is_magic(new_grid):
                    ans += 1

    
        return ans 
    

    def is_magic(self, grid):
        seen = set()
        for r in range(0,3):
            for c in range(0, 3):
                if grid[r][c] in seen or (grid[r][c] > 9 or grid[r][c] < 1):
                    return False
                seen.add(grid[r][c])
        for each in grid:
            total = sum(each)
          
            if total != 15:
                return False
        
        for i in range(0, 3):
            total = grid[0][i] + grid[1][i] + grid[2][i]
            
            if total != 15:
                return False
        
        diag_1 = grid[0][0] + grid[1][1] + grid[2][2]
        if diag_1 != 15:
            return False
        diag_2 = grid[0][2] + grid[1][1] + grid[2][0]
        if diag_2 != 15:
            return False
        return True
        