class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["*", "-", "+", "/"]
        res = 0
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                a= int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == "*":
                    stack.append(a*b)
                elif tokens[i] == "+":
                    stack.append(a+b)
                elif tokens[i] == "/":
                    stack.append(int(b / a))
                else:
                    stack.append(b-a)
        return stack[0]