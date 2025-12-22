import heapq

def topk_heap(nums, k):
    count = {}
    for each in nums:
        count[each]  = 1 + count.get(each, 0)

    heap = []

    for key, val in count.items():
        heapq.heappush(heap, (val, key)) # (freq, number)
        if len(heap) > k:
            '''
            idea is to keep just k elements 
            so it will pop out smaller values than top k values 
            '''
            heapq.heappop(heap) 
    
    res = []

    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


ip = [1,1,1,1,1,2,3,4,2,2,44,1,4,111,23,2,2,2,2,2,2,4]
k = 2
op = topk_heap(ip, k)
print(op)
    