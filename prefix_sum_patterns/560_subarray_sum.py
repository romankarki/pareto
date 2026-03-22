from typing import List 


class Solution: 


    def subarray_sum(self, nums: List[int], k: int) -> int: 
        res = curr_sum = 0 
        prefix_sums = {0: 1}

        for num in nums: 
            curr_sum += num 
            diff = curr_sum - k 
            res += prefix_sums.get(diff, 0)
            print("res becomes", res)
            prefix_sums[curr_sum] = 1+ prefix_sums.get(curr_sum, 0)
            print("prefix Sum becomes", prefix_sums)
            print("-------------------------")
        
        print("Prefix Sum at the end =", prefix_sums)
        return res 
    

    def subarray_sum_revision(self, nums: List[int], k: int) -> int:
        res = running_sum = 0 
        seen = {0: 1}
        '''
        [1, 2, 3], 3
        0 -> 1 
        '''

        for num in nums:
            running_sum += num 
            diff = running_sum - k 
            res += seen.get(diff, 0) 
            seen[running_sum] = 1 + seen.get(running_sum, 0)
        
        return res  
    



s = Solution()
print(s.subarray_sum([1,2,3], 3))