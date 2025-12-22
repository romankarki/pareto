class ListNode:

    def __init__(self, val=[], next = None):
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.llist = None


    def get(self, key: int):

        head = self.llist
        prev = None
        ans = -1
        while(head):
            if(head.val[0] == key):
                ans = head.val[1]
                break
            prev = head 
            head = head.next
        prev.next = prev.next.next
        
        return ans
            
                    


    def put(self, key:int, value:int) :
       new_node = ListNode([key, value]) 

       new_node.next = self.llist
       head = new_node
       for _ in range(self.capacity - 1):
            head = head.next
       head.next = None
       self.llist = new_node