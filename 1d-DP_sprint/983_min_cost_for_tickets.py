from typing import List 


class Solution: 


    def min_cost_for_tickets(self, days: List[int], costs: List[int]) -> int: 
        '''
        input 
            days = [1, 4, 6, 7, 8, 20] #out of 365

            costs = [2, 7, 15] #1day, 7day, 30day
        '''

        def dfs(i: int) -> int: 
            if i == len(days):
                return 0 
            
            j = i 

            while j < len(days) and days[j] < days[i] + 1: 
                j += 1
            cost1 = costs[0] + dfs(j)
        
            j = i 

            while j < len(days) and days[j] < days[i] + 7: 
                j += 1
            cost7 = costs[1]  + dfs(j)


            j = i 
            while j < len(days) and days[j] < days[i] + 30: 
                j += 1
            cost30 = costs[2] +dfs(j)

            return min(cost7, cost30, cost1)

        return dfs(0)
    


    def min_cost_concise(self, days: List[int], costs: List[int]) -> int:
        '''
        input 
            days = [1, 4, 6, 7, 8, 20] #out of 365

            costs = [2, 7, 15] #1day, 7day, 30day
        ''' 
        self.CC = [1, 7, 30]
        print("Days", days)
        print("Costs", costs)
        def dfs(i: int) -> int:
            print(" --------------------------------------------")
            if i == len(days): 
                return 0 
            res = float('inf')

            for ind, c in enumerate(costs): 
                j = i 
                print(" i = ", i)
                print(" j = ", j)

                while j < len(days) and days[j] < days[i] + self.CC[ind]:
                    print("days[j] = ", days[j])
                    print("passs -->", self.CC[ind])
                    print("days[i] +",self.CC[ind],"=", days[i] + self.CC[ind]) 
                    j += 1
                
                print("finally dfs ing  j as", j)
                res = min(res, c + dfs(j)) 
            return res
        return dfs(0)
    

s = Solution()

print(s.min_cost_concise([1,4,6,7,8,20], [2, 7, 15]))