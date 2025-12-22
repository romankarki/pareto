from typing import List

def daily_temp(temps:List)->List:
    '''
    we can just brute force for O(n^2)

    but for tempearatures we can solve as a stack problem 
    use the concept of monotonic stack
    '''
    result = [0] * len(temps)

    stack = [] 
    # stack in pairs like [val, index]

    for i, val in enumerate(temps):
        while stack and val > stack[-1][0]:
           stack_val, stack_ind = stack.pop()
           result[stack_ind] = i - stack_ind

        
        stack.append((val, i))

    return result



    