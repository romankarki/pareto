from typing import List
import heapq
from collections import Counter

class Revision: 

    def kth_largest_pattern1_1(self, arr: List[int], k: int) -> int: 
        '''
        arr = [3,2,1,5,6,4]
        k = 2 
        output  = 5
        '''
        heap = []

        for each in arr: 
            heapq.heappush(heap, each)
            if len(heap) > k: 
                heapq.pop()
        return heap[0]


    def kth_largest_pattern1_2(self, arr: List[int], k: int) -> int: 
        # O(n log(n))
        heap  = []
        for each in arr: 
            heapq.heappush(heap, each)

            if len(heap) > k : 
                heapq.heappop()

        return heap[0]


    def k_freq_element_pattern2_1(self, arr: List[int], k: int) -> int: 
        '''
            arr = [1,1,1,2,2,3]
            k = 2 
            output = [1,2]
        '''
        freq = Counter(arr)
        heap = []

        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [num for _, num in heap]
    

    def k_freq_element_pattern2_2(self, arr: List[int], k: int) -> int:
        # O(n) + O(log(n)) => O(n) 
        heap = []

        freq = Counter(arr)

        for k, v in freq.items():

            heapq.heappush(heap, (v, k))
            if len(heap) > k: 
                heap.pop()


        return [num for _,num in heap ]

    def kth_largest_arr_pattern1_3(self, nums: List[int], k: int) -> int: 
        heap = []


        for each in nums: 
            heapq.heappush(heap, each)
            if len(heap) > k: 
                heapq.heappop(heap)
        return heap[0]


    def k_freq_element_arr_pattern2_3(self, nums: List[int], k: int) -> int: 


        heap  = [] 

        freq = Counter(nums) #o(n)

        #O(log(n))
        for num, f in freq.items():
            heapq.heappush(heap, (f, num))

            if len(heap) > k: 
                heapq.heappop()


        return [num for _, num in heap] 
    


    def merge_k_sorted_pattern3_1(self, lists: List[List[int]]) -> List[int]: 
        '''
        lists = [[1,4,5], [1,3,4], [2,6]]
        output = [1,1,3,3,4,4,5,6]
        '''
        #basically push and pop and at the same time 
        heap = []
        res = []

        for i, lst in enumerate(lists): 
            heapq.heappush(heap, (lst[0], i, 0))
        

        while heap:
            val, i, j = heapq.heappop(heap)
            res.append(val)
            if j + 1 < len(lists[i]): 
                heapq.heappush(heap, (list[i][j+1], i, j+1))
        return res 


    def merge_k_sorted_pattern3_2(self, lists: List[List[int]]) -> List[int]: 

        res = []
        heap = []
        for i, lst in enumerate(lists): 
            heapq.heappush(heap, (lst[0], i, 0))
        

        while heap:
            val, i, j = heapq.heappop(heap)
            res.append(val)

            if j + 1 < len(lists[i]): 
                heapq.heappush(heap, (lists[i][j+1], i, j+1))
    

        return res


class MedianStrem:


    def __init__(self): 
        self.small = [] # max
        self.large = [] # min
        # [1,2,3,4,5,6,7,8,9]
        # small => [-5, -4,-3,- 2, -1]
        # large => [6, 7, 8, 9, 10]

    def add(self, num: int): 
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, - heapq.heappop(self.small))

        if len(self.large) > len(self.small): 
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def median(self):
        if len(self.small) > len(self.large): 
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
    
    def add_num(self, num: int): 
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, - heapq.heappop(self.small))

        if len(self.large) > len(self.small): 
            heapq.heappush(self.small, - heapq.heappop(self.large))

    

    def median_cal(self): 
        if len(self.small) > len(self.large):
            return - self.small[0]


        return (- self.small[0] + self.large[0]) / 2




    

    


        

