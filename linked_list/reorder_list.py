from typing import Optional

class ListNode: 
    def __init__(self, val = 0, next = None): 
        self.val = val
        self.next = next 

def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]: 
    '''
    challenge is to change the same reference head by not creating another 
    put all of the nodes in array and do it as a two pointer


    '''

    if not head: 
        return None
    
    nodes = []

    curr = head 
    while curr: 
        nodes.append(curr)
        curr = curr.next 
    
    l, r = 0, len(nodes)- 1

    while l < r:
        nodes[l].next = nodes[r]
        l += 1
        if(l >= j): 
            break
        nodes[r].next = nodes[l]
        r -= 1
    nodes[l].next = None
