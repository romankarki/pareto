import heapq
from collections import Counter

class Solution:

    def reorganize_string(self, s: str) -> str:
        counts = Counter(s)

        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        result = [] 

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            result.append(ch1)
            result.append(ch2)

            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1+1, ch1))
            if cnt2 + 1 < 0: 
                heapq.heappush(heap, (cnt2 + 1, ch2))

        if heap:
            cnt, ch = heap[0]
            if -cnt > 1:
                return "" # impossible 
            result.append(ch)

        return "".join(result)
    

    def reorganize_string_revision_1(self, s: str) -> str:

        '''
            abcacbcacbc
            a 3
            b 3
            c 5  -> c5, a3, b3 -> c4, a2, b3 -> c3, a2, b2 -> c2, a1, b2+ c1 a1 b1 -> c

            ca + cb + ca + cb + ab + c => cacbcacbabc
        
        '''
        
        counts = Counter(s)
        result = []
        heap = [(-cnt, ch) for cnt, ch in counts.items()]
        heapq.heapify(heap)

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)
            result.append(ch1)
            result.append(ch2)

            cnt1 = cnt1 + 1 
            cnt2 = cnt2 + 1
            if cnt1 < 0: 
                heapq.heappush((cnt1, ch1))
            if cnt2 < 0:
                heapq.heappush((cnt2, ch2))

        while heap:
            cnt, ch = heap[0]
            if -cnt > 1: 
                return ""
            result.append(ch)


        return "".join(result)
    


    def reorganize_string_revision2(self, s: str) -> str: 

        result = []
        c = Counter(s)
        heap = [(-cnt, ch) for ch, cnt in c.items()]
        heapq.heapify(heap)

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            result.append(ch1)
            result.append(ch2)

            cnt1 += 1
            cnt2 += 1

            if cnt1 < 0 :
                heapq.heappush(heap, (cnt1, ch1))
            if cnt2 < 0:
                heapq.heappush(heap, (cnt2, ch2))

        if heap:
            cnt, ch = heapq.heappop(heap)
            if -cnt > 1:
                return ""

            result.append(ch)
        
        return "".joing(result)