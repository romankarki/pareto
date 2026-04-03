from typing import List 

class Solution:


    def container_most_water(self, height: List[int]) -> int:
        l, r = 0, len(height) -1 

        max_area = 0 
        ans = [0, 0]
        while l < r:
            length = r - 1
            short_height = min(height[l], height[r])
            area = length * short_height

            
            max_area = max(max_area, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r += 1

        return max_area
    

    def container_most_water_revision_1(self, height: List[int]) -> int: 
        l, r = 0, len(height) - 1

        result = 0 
        while l < r:
            area = (r-l) * min(height[l], height[r])
            result = max(area, result)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return result 