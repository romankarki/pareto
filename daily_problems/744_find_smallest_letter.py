from typing import List 


class Solution: 


    def next_greater(self, letters: List[str], target: str) -> str:

        smallest = letters[0] 

        for each in letters: 
            
            if ord(target) < ord(each):
                smallest = each 
                break 
        return smallest 