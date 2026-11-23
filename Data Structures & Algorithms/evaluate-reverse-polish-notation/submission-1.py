class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #stack store operators
        #two operands from stack
        #while stack

        stack = []
        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                val1 = stack.pop() #avoid pop from empty list error, problem constraints, given op first
                val2 = stack.pop()
                if token == "+":
                    stack.append(val1+val2)
                elif token == "-":
                    stack.append(val2-val1)
                elif token == "*":

                    stack.append(val1*val2)
                elif token == "/":
                    stack.append(int(val2/val1)) #truncate toward zero
            else:
                    stack.append(int(token))       
        return stack[-1]         


        