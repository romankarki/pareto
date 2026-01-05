from typing import List

class Solution:

    def max_matrix_sum(self, matrix: List[List[int]]) -> int:

        '''
        - count negative
        - even: abs_sum 
        - odd: abs_sum - 2(minimum)
        '''
        count_neg = 0 
        abs_sum = 0
        mini = float('inf')
        R, C = len(matrix), len(matrix[0])

        for r  in range(0, R):
            for c in range(0, C):
                curr = matrix[r][c]
                abs_sum += abs(curr)
                mini = min(mini, abs(curr))
                if curr < 0:
                    count_neg += 1
        
        if count_neg % 2 == 1:
            return abs_sum - (2*mini)
        return abs_sum 



s = Solution()
i= [
    [1,2,3],
    [-1,-2,-3],
    [1,2,3]
]

print(s.max_matrix_sum(i))