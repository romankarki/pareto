from typing import List 
from collections import deque

class Solution:


    def oranges_rotting(self, grid: List[List[int]]) -> int:

        time = 0 
        fresh = 0 

        R, C = len(grid), len(grid[0])
        q = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        while q and fresh > 0:
            epoch = len(q)

            for _ in range(epoch):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if not(0 <= nr < R) or not(0 <= nc < C) or grid[nr][nc] != 1:
                        continue 
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))

            time += 1

        return time if fresh == 0 else -1