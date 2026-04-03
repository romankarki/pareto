class Solution:


    def is_valid(self, s:str) -> bool:
        brac_dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        opening = set(["(","{","["])
        stack = []

        for each in s:
            if each in opening:
                stack.append(each)
                continue
            popped = stack.pop()
            if brac_dict[each] == popped:
                continue 
            else:
                return False  

        return True if len(stack) == 0 else False 