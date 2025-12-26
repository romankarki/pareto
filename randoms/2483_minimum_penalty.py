class Solution:

    def min_penalty(self, customers : str) -> int:

        total_penalty = 0 
        for each in customers:
            if each == "Y":
                total_penalty += 1
        
        ans = [0, total_penalty]
        hour = 0 

        for i in range(0, len(customers)):
            hour += 1

            penalty = total_penalty
            if customers[i] == "Y":
                penalty -= 1
                total_penalty -= 1
            else:
                penalty += 1
                total_penalty += 1
            
            if penalty < ans[1]:
                ans = [hour, penalty]
            

        return ans[0] 