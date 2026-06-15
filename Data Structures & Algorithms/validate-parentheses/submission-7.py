class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"{" : "}", "(" : ")", "[": "]"}
        left = 0
        for brac in s:
            if brac in mydict:
                stack.append(brac)
            else:
                if not stack:
                    return False    
                if not brac == mydict[stack.pop()]:
                    return False
                else:
                    left+=1

        return len(stack) == 0 