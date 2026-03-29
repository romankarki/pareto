from typing import List 
from collections import deque
class BFS_PATTERNS:

    def rotten_oranges(self, grid: List[List[int]]) -> int: 

        time = 0 
        fresh = 0 
        q = deque()

        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        

        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        while fresh > 0 and q:
            epoch = len(q)
            for i in range(epoch):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if not(0 <= nr < R) or not (0 <= nc < C) or grid[nr][nc] == 0:
                        continue
                    if grid[nr][nc] == 1:
                        fresh -= 1 
                        q.append((nr, nc))
                        grid[nr][nc] = 2 
            time += 1
        return time if fresh == 0 else -1  


class DFS_PATTERNS:
    
    def num_of_islands(self, grid) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        R, C = len(grid), len(grid[0])
        islands = 0 

        def traverse(r, c):
            if not(0 <= r < R) or not(0 <= c < C) or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                traverse(nr, nc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    traverse(r, c)
                    islands += 1
        return islands