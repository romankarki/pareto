from typing import List

class Preparation_Week_1:


    def rotate_matrix(self, matrix: List[List[int]]) -> List[List[int]]:

        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        

        for row in matrix: 
            row.reverse()
    


    def spiral_matrix(self, matrix: List[List[int]]) -> List[List[int]]:

        res = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1


        while top <= bottom and left <= right: 
            for c in range(left, right+1):
                res.append(matrix[top][c])
            top += 1

            for r in range(top, bottom+1):
                res.append(matrix[r][right])
            right -= 1


            if top <= bottom:
                for c in range(right, left -1 ,- 1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            
            if left <= right: 
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
            

        return res
    


    #Graphs

    def bfs_grid(self, grid: List[List[int]]):

        from collections import deque

        rows, cols = len(grid), len(grid[0])

        q = deque([(0,0,0)])
        visited = {(0,0)}

        while q:
            r, c, d = q.popleft()

            if r == rows -1 and c == cols - 1:
                return d
            
            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0<=nr < rows and 0<= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, d+1))

        return -1



    #Greedy best time to buy stocks

    def max_profil(self, prices: List[int]): 
        min_price = float('inf')

        profit = 0 

        for p in prices: 
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)

        return profit 


    #dfs-> num islands

    def num_islands(self, grid: List[List[int]]) -> int: 

        R, C  = len(grid), len(grid[0])


        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c -1) 

        count = 0 

        for r in range(R):
            for c in range(C):
                if grid[r][c] =="1":
                    dfs(r,c)
                    count +=1
        return count 