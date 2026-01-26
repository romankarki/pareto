from typing import List

class NumMatrix:


    def __init__(self, matrix: List[List[int]]): 
        rows, cols = len(matrix), len(matrix[0])
        pre = [[0] * (cols+1) for _ in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                pre[i][j] = matrix[i-1][j-1] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1]
        

        self.prefix = pre



    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int: 

        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
    



class Num2D:

    def __init__(self, mat: List[List[int]]):

        R, C = len(mat), len(mat[0])
        self.pre_sum = [[0] * (C+1) for _ in range(R+1)]

        for r in range(R):
            running_sum = 0 
            for c  in range(C):
                running_sum += mat[r][c]
                above = self.pre_sum[r][c+1]
                self.pre_sum[r+1][c+1] =  running_sum + above
    


    def sumRegion(self, r1, c1, r2, c2): 
        r1, r2, c1, c2 = r1+1, r2+1, c1+1, c2+1

        bottom_right = self.pre_sum[r2][c2]
        top_left = self.pre_sum[r1-1][c1-1]
        above = self.pre_sum[r1-1][c2]
        left = self.pre_sum[r2][c1-1]
        

        return bottom_right - above  - left + top_left 