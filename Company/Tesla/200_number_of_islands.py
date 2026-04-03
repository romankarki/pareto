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
            q = deque()
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


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    traversal(r, c)
                    islands += 1
        return islands