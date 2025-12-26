from typing import List 


class Solution:


    def make_square(self, match_sticks: List[int]) -> bool:
        total = sum(match_sticks)
        if total % 4 != 0:
            return False
        
        sides = [0] * 4

        def dfs(i):
            if i == len(match_sticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for side in range(4):
                sides[side] += match_sticks[i]
                if sides[side] > total:
                    sides[side] -= match_sticks[i]
                    return False
                if dfs(i+1):
                    return True
                sides[side] -= match_sticks[i]
            return False



        return dfs(0)
    




test1 = [[1,3,4,2,2,4], True]
test2 = [[1,5,6,3], False]

s = Solution()

print("Passed :",s.make_square(test1[0]) == test1[1])
print("Passed :",s.make_square(test2[0]) == test2[1])