def min_rotated_array(nums):
    '''
    so characteristics of target is that 
    nums[mid -1] > nums[mid]
    for case of already sorted 
    [1, 2, 3, 4, 5, 6 ]
    '''

    l, r = 0, len(nums) -1 
    res  = nums[0]
    while(l <= r):
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r) //2 
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else: 
            r = m - 1
    return res



ip  = [3, 4, 5, 1, 2]

ip2 = [7, 8, 2,3, 4, 5, 6]

op1 = min_rotated_array(ip2)
print(op1)