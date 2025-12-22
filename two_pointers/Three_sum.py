def three_num_sum(nums):
    nums.sort()
    ans = []
    for i, a in enumerate(nums):
        if( a > 0): 
            break

        l, r = i+1, len(nums) - 1
        req = 0 - a

        if( l > 0 and nums[l-1] == nums[l]): 
            continue


        while l < r: 
            total = nums[l] + nums[r]

            if(total == req):
                ans.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l-1] == nums[l] and l < r: 
                    l += 1
                continue 
                
            if(total > req): 
               r -= 1 
            else:
                l += 1
    return ans 


