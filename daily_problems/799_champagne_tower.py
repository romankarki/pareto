class Solution:



    def champagne_tower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        champagne doesn't flow level by level - keep that in mind -> was wrong initially on that 
        '''

        tower = [[0.0 for _ in range(i+1)] for i in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(row+1):
                overflow = (tower[row][glass] - 1.0)/2.0
                if overflow > 0:
                    tower[row+1][glass] += overflow
                    tower[row+1][glass+1] += overflow
        


        return min(1.0, tower[query_row][query_glass])