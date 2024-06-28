# https://leetcode.com/problems/validate-stack-sequences/description/

def evalRPN(self, tokens) -> int:
    stack = []
    for i in tokens:
        if i.isnumeric() or (i[0] == '-' and i[1:].isnumeric()):
            stack.append(int(i))
            
        if i == "-":
            s = stack.pop()
            f = stack.pop()
            stack.append(int(f-s))
        elif i == "+":
            s = stack.pop()
            f = stack.pop()
            stack.append(int(f+s))
        elif i == "*":
            s = stack.pop()
            f = stack.pop()
            stack.append(int(f*s))
        elif i == "/":
            s = stack.pop()
            f = stack.pop()
            stack.append(int(f/s))
    
    #now there should only be 1 integer in the stack
    return stack.pop()



    """
    push numbers on to a stack
    when you see an operator, remove the last two items in the stack
    perform the operation and add them back to the stack
    when you've gone through the whole input list you should only have 
    one number on the stack. pop that and return it. 
    """
    