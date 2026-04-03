from typing import List
from collections import deque

class Solution:

    def num_islands(self, grid: List[List[int]])->int:
        dirs = [
            [-1, 0], [1, 0], [0, -1], [0, 1]
        ]

        R, C = len(grid), len(grid[0])
        islands = 0 

        def traversal(r, c):
            #bfs 
            q = deque([])
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc 
                    if  not(0 <= nr < R) or not(0 <= nc < C) or grid[nr][nc] == "0":
                        continue 
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        
        def traversal_dfs(r, c):
            if not (0 <= r < R) or not(0 <= c < C) or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc 
                traversal_dfs(nr, nc)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    traversal(r, c)
                    islands += 1
        return islands
    

    def num_of_islands_revision(self, grid: List[List[str]]) -> int:
        islands = 0 
        dirs = [
            [-1, 0], [1, 0], [0, -1], [0, 1]
        ]
        R, C = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r,c)])
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc 
                    if not (0 <= nr < R) or not(0 <= nc < C) or grid[nr][nc] == "0" : 
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
        

        def dfs(r, c):
            if grid[r][c] == "0" or not (0 <= r < R) or not (0 <= c < C):
                return 
            grid[r][c] = "0"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)



        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands