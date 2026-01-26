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