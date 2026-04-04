class Solution:

    def isHappy(self,  n: int) -> bool:
        n_set = set()
        while n not in n_set:
            sum_of_squares = 0 
            n_set.add(n)
            while n != 0 :
                digit = n % 10 
                sum_of_squares += digit ** 2
                n =  n // 10
            if sum_of_squares == 1:
                return True 
            n = sum_of_squares
        return False 