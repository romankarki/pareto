def prod_not_self(nums):
    '''
    if we brute force then this will be o(n^2)
    if we do a cummulative product and dedcut each we can achieve o(n)
    but cases are 0 and negatieves ( don't care about negatives )
    but care about 0s 
    if one zero just one product
    if multiple zeros then all zeros 
    '''

    zero_cnt, prod = 0, 1
    for num in nums:
        if( num == 0): 
            zero_cnt += 1
    
    if(zero_cnt >= 2): 
        prod = 0 
        ans = [0] * len(nums)
        return ans
    
    for num in nums:
        if(num != 0):
            prod *= num 
    

    ans = []
    for num in nums: 
        if(zero_cnt and num != 0):
            ans.append(0)
            continue
        elif(zero_cnt and num == 0):
            ans.append(prod)
            continue
        
        curr = prod // num 
        ans.append(curr)



    return ans

ip1 = [1,2,3,4]
op1 = [24, 12, 8, 6]

ip2 = [-1, 1, 0, -3, 3]
op2 = [0, 0, 9, 0, 0]