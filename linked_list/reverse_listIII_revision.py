class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next


def reverse_between(head, left, right):
    '''
        * first separate the sublist from left to right 
        * reverse the sublist 
        * join the ends in reverse order as needed  
    '''
    #calculating sublist to be reversed
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy 

    for _ in range(left - 1): 
        prev = prev.next
    
    sublist_head = prev.next
    sublist_tail = sublist_head
    for _ in range(right - left): 
        sublist_tail = sublist_tail.next
    
    #detaching ends for later joins
    next_node = sublist_tail.next
    sublist_tail.next = None

    reveresed_sublist = reverse_lllist(sublist_head)

    #now join correct reveresed ends 
    prev.next = reveresed_sublist
    sublist_head.next = next_node

    return dummy.next
    
    
def reverse_lllist(head): 
    curr, prev = head, None 
    while curr : 
        temp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = temp 
    return prev 

    