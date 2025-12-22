from typing import Optional 

class ListNode: 
    def __init__(self, val = 0, next = None):
        self.next = next
        self.val = val



class Solution: 

    def cycle_detection(self, head: Optional[ListNode]) -> bool: 
        if head == None: 
            return False
        
        slow, fast = head, head

        while slow and fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
            if(slow == fast): 
                return True
        return False