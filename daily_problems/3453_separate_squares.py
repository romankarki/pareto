from typing import List

class Solution: 

    def separate_squares(self, squares: List[List[int]]): 
        total_area = sum(l*l for _, _, l in squares)
        target = total_area / 2.0 

        min_y = min(y for _, y, _ in squares)
        max_y = max(y+l for _, y, l in squares)


        low = float(min_y)
        high = float(max_y)


        for _ in range(60):
            mid = (low + high) / 2
            current_area = 0.0 

            for _, y, l in squares:
                if mid > y:
                    height_below = min(mid - y, float(l))
                    current_area += height_below * l 
            if current_area >= target:
                high = mid 
            else: 
                low = mid
        return high 

    


    def separate_squares_i(self, squares: List[List[int]]) -> float: 
        total_area = sum(l*l for _, _, l in squares)

        half = total_area / 2.0

        low, high = min(y for _,y,_ in squares), max(y+l for _,y,l in squares)

        def area_below(h:int): 
            area = 0 
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += (h-y) * l 
            return area 
        
        while (high - low) > 1e-6:
            mid = (low + high) / 2
            if area_below(mid) < half: 
                low = mid
            else:
                high = mid
        return low 

    

    


    