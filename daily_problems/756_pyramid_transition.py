from typing import List

class Solution:

    def pyramid(self, bottom: str, allowed: List[str]) -> bool:

        memo = set()
        def backtrack(level: int, b: str, n: int, new_b: str):

            state = (b, n, new_b) # bottom, index, new_bottom
            if state in memo:
                return False
            
            if len(b) == 1:
                return True

            for each in allowed:
                to_check = each[0] + each[1]
                from_bottom = b[n] + b[n+1]
                if to_check == from_bottom:
                    if n == (level - 1):
                        if backtrack(level-1, new_b+each[2],0 , ""):
                            return True
                    else:
                        if backtrack(level, b, n+1, new_b+each[2]):
                            return True
            
            memo.add(state)

            return False
        
        return backtrack(len(bottom)-1, bottom, 0, "")
                        
                

s = Solution()
print(s.pyramid("bcd", ["bcc","cde","cea", "fff"]))
                        
