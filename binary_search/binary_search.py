def binary_search(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while(l <= r):
        mid = (l+r)//2
        if(nums[mid] == target): 
            return mid 
        elif(nums[mid] > target):
           r = mid-1 
        elif(nums[mid] < target):
           l = mid+1 
    return -1 



ip = [-1,0, 1,9, 21,11, 10, 111]
target  = 9 
ans = binary_search(ip, target)
print(ans)