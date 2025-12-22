class ListNode: 
   def __init__(self, val = 0, next = None): 
      self.val = val
      self.next = next

def reverse(head, left, right): 
    dummy = ListNode(0)
    dummy.next = head 
    prev = dummy 
    for _ in range(left - 1): 
       prev = prev.next 

    sublist_head = prev.next 
    sublist_tail = sublist_head 

    for _ in range(right - left): 
       sublist_tail = sublist_tail.next
    
    next_node = sublist_tail.next
    sublist_tail.next = None
    reveresed_sublist = reverseList(sublist_head)
    prev.next = reveresed_sublist
    sublist_head.next = next_node


    return dummy.next 



def reverseList(head): 
    prev, curr = None, head 

    while curr:
       temp = curr.next 
       curr.next = prev 
       prev = curr 
       curr = temp 
    
    return prev  
    