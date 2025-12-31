from typing import List
from collections import deque

class Solution:

    def last_day(self, row: int, col: int, cells: List[List[int]]) ->  int:

        left, right = 1, len(cells)
        ans = 0 
        while left <= right:

            mid = (left + right )// 2
            if self.can_cross(row, col, mid, cells):
                ans = mid 
                left = mid + 1
            else:
                right = mid - 1
        return ans 
    

    def can_cross(self, row: int, col: int, day: int, cells: List[List[int]]) -> bool:
        grid = [[0] * col for _ in range(row)]

        for i in range(day):
            r, c = cells[i]
            grid[r-1][c-1] = 1 # flooded
        
        q = deque()
        for j in range(col):
            if grid[0][j] == 0:
                q.append((0, j))
                grid[0][j] = -1 # marking visited
        
        while q:
            x, y = q.popleft()
            if x == row - 1:
                return True
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx , y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                    q.append((nx, ny))
                    grid[nx][ny] = -1 # visited
        return False