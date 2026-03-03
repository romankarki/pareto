from typing import List


class Solution:
     

    def min_swaps(self, grid: List[List[int]]) -> int: 
        n = len(grid)
        trailing = []

        for row in grid:
            count = 0 
            for j in range(n-1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        swaps = 0 

        for i in range(n):
            need = n - 1 - i
            found = -1

            for j in range(i, n):
                if trailing[j] >= need:
                    found = j 
                    break
            if found == -1:
                return -1
            
            while found > i:
                trailing[found], trailing[found - 1] = trailing[found-1], trailing[found]
                found += 1
            
        
        return swaps 



    def repeat_min_swaps(self, grid):

        n = len(grid) # total number of rows

        trailing = []

        for row in grid:
            count= 0 
            for j in range(n-1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0 

        for i in range(n):

            need = n - 1 - i

            found = -1  

            for j in range(i, n):

                if trailing[j] >= need:
                    found = j 
                    break 


            if found == -1:
                return -1 
            
            while found > i:
                trailing[found], trailing[found -1] = trailing[found-1], trailing[found]
                found -=1 
                swaps += 1
        return swaps