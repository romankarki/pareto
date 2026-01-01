from typing import List

class Solution:

    def plus_one_personal_sol(self, digits: List[int]) -> List[int]:
        ans = [] 

        l, r = 0, len(digits) - 1

        digits[r] += 1

        while l <= r:
            if digits[r] <= 9:
                break
            remain = digits[r] % 10
            forward = digits[r] // 10

            digits[r] = remain
            if (r-1) < l:
                ans.append(forward)
            else:
                digits[r-1] = digits[r-1] + forward
            
            r -= 1
        


        return ans + digits




s = Solution()

op = s.plus_one_personal_sol([1,2,9,9])
print(op)