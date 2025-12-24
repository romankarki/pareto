from typing import Optional
import heapq


class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = None 

class IntegerContainer:
    def __init__(self):
        self.container = None 
        self.head = None 
        self.tail = None 
        self.len = 0
        self.call_stack = []
        self.operations = ["add", "delete"]

        self.opposite ={
            "add":"delete",
            "delete": "add"
        }
        
        

    def add(self, num: int ) -> int:
        if(self.container):
            new_node = ListNode(num)
            self.tail.next = new_node
            self.tail = self.tail.next 
        if(not self.container and self.len == 0):
           self.container = ListNode(num)
           self.head = self.container
           self.tail = self.container

        self.len += 1
        self.call_stack.append(("add", num))
        return self.len
    

    def delete(self, num: int) -> bool:
        node = self.head 
        if(not self.container):
            return False
        if(self.container.val == num):
            tmp  = self.container.next
            self.head = tmp 
            self.container.next = None 
            self.container = tmp 
            if(self.len == 1):
                self.tail = tmp
            self.len -= 1
            self.call_stack.append(("delete", num))
            return True
        
        while(node and node.next):
            curr = node.next.val 
            if(curr == num):
                node.next = node.next.next
                if(not node.next):
                    self.tail = node
                self.len -= 1
                self.call_stack.append(("delete", num))
                return True
            node = node.next
        return False
    
    def print_ds(self):
        h = self.head
        while h:
            print(h.val)
            print("    ||    ")
            h = h.next
        print("End of print ------")
    
    def undo(self): 
        if len(self.call_stack) == 0:
            return False
        op, val = self.call_stack.pop()
        print("undoing", op,"for", val)
        if op == "add":
            self.delete(val) 
        elif op == "delete":
            self.add(val) 




c = IntegerContainer()
c.add(5)
c.add(10)
c.add(100)
c.add(400)
c.add(1000)
c.delete(5)
c.print_ds()
c.undo()
print("undoing")
c.print_ds()

# c.delete(100)
# c.delete(200)
# print("---------------After all operation ------------------------")
# c.print_ds()
