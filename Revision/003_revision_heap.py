from typing import List
import heapq

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
    

    


        

