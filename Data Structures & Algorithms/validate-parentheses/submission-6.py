class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            if s[i] == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()                                 
            if s[i] == ']':
                #print(stack[-1])
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            i+=1
        if len(stack) == 0:
            return True
        else:
            return False
                        
        #REMEMBER TO CHECK ALL EDGE CASES