from typing import List


class Solution: 


    def sep_squares_ii(self, squares: List[List[int]]) -> float: 


        def union_area(rects): 
            events = []

            for x1, y1, x2, y2 in rects: 
                events.append((y1, 1, x1, x2))
                events.append((y2, -1, x1, x2))
            events.sort()

            active = []

            prev_y = events[0][0]
            area = 0 

            def merged_width(intervals):
                intervals.sort()
                total = 0 
                cur_l, cur_r = intervals[0]
                for l, r in intervals:

                    if l > cur_r: 
                        total += cur_r - cur_l 
                        cur_l, curl_r = l, r
                    else: 
                        cur_r = max(cur_r, r)
                total += cur_r - cur_l 
                return total 

            for y, typ, x1, x2 in events: 
                dy = y - prev_y 
                if dy > 0 and active: 
                    area += dy * merged_width(active)
                
                if typ == 1:
                    active.append((x1, x2))
                else: 
                    active.remove((x1, x2))
                prev_y = y 
            return area 


        def area_below(h):
            rects = []
            for x, y, l in squares:
                if y >= h:
                    continue
                rects.append((
                    x, y, x+l, min(y+l, h)
                ))
            if not rects: 
                return 0.0 
            return union_area(rects)

        full_rects = [(x, y, x+l, y+l) for x,y,l in squares]
        total_area = union_area(full_rects)
        half = total_area / 2.0 

        low, high = min(y for _, y, _ in squares), max(y+l for _, y, l in squares)

        eps = 1e-6

        while high - low > eps:
            mid = (low + high) / 2

            if area_below(mid) < half:
                low =  mid
            else: 
                high = mid
        return low 

# too dificcult can be skipped



