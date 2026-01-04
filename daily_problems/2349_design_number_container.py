from collections import defaultdict
import heapq

class Solution:


    def __init__(self):
        self.index_to_num = {}
        self.num_to_index = defaultdict


    def change(self, index: int, number: int) -> None :
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_index[number], index)


    def find(self, number: int) -> int:
        if number not in self.num_to_index:
            return -1
        heap = self.num_to_index[number]
        while heap:
            if self.index_to_num.get(heap[0]) == number:
                return heap[0]
            heapq.heappop(heap)
        return -1