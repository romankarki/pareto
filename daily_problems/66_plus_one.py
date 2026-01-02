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
    

    def plus_one_pythonic(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0 
        
        return [1] + digits




s = Solution()

# op = s.plus_one_personal_sol([1,2,9,9])
op = s.plus_one_pythonic([1,2,9,9,9])
print(op)