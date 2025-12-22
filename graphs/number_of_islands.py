from typing import List
from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            [-1,0],[1,0],[0,1],[0,-1]
        ]

        if len(grid) == 0 : 
            return 0 
        
        if len(grid[0]) == 0:
            return 0 
        
        R, C = len(grid), len(grid[0])

        islands = 0 

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"

            q.append((r,c))
            while q: 
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == "0" :
                        continue
                    q.append((nr,nc))
                    q[nr][nc] = "0"
        


        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == "0":
                return 

            grid[r][c] = "0"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                dfs(nr, nc) 


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1


        return islands 