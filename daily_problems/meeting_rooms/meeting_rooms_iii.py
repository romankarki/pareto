from typing import List

class Solution:

    def most_booked(self, n: int, meetings: List[List[int]]) -> int:
        counts = [0] * n
        rooms = [0] * n

        meetings.sort()

        for s, e in meetings:
            min_room = 0 
            found = False
            for i in range(n):
                if rooms[i] <= s:
                    found = True 
                    counts[i] += 1
                    rooms[i] = e
                    break 
                if rooms[min_room] > rooms[i]:
                    min_room = i 
            if found:
                continue 
            counts[min_room] += 1
            rooms[min_room] += e-s
        
        target = max(counts)
        for i, each in enumerate(counts):
            if each == target:
                return i 
        return 0