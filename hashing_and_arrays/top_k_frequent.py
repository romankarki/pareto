# import heapq

def top_k_frequent(nums, k):
    '''
    count -> freq of all nums 
    we sort values in arra like [[freq, num] .....]
    and we sort it again 
    and then pop k elements ffrom it 
    so i.e. 
    time -> O(n log(n))
    space -> O(n)
    '''
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []

    while(len(res) < k):
        res.append(arr.pop()[1])
    
    return res 





ip = [1,1,1,1,1,2,3,4,2,2,44,1,4,111,23,2,2,2,2,2,2,4]
k = 2
op = top_k_frequent(ip, k)
print(op)
    