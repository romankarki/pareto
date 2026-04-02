class Solution: 


    def basic_calculator_ii(self, s: str) -> int: 
        stack = []
        num = 0 
        prev_op = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in '+-*/' or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / num))
                prev_op = ch 
                num = 0 
        
        return sum(stack)
    
    def basic_calculator_revision_1(self, s: str) -> int: 
        stack = []
        num = 0 
        prev_op = "+"

        for i, ch in s: 
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in '+-*/':

                if prev_op == "+":
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num )
                elif prev_op == '/':
                    stack.append(int(stack.pop()/ num))
                prev_op = ch 
                num = 0 

        return sum(stack)
        