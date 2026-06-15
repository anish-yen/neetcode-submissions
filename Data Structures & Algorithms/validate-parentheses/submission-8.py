class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"{" : "}", "(" : ")", "[": "]"}

        for brac in s:
            if brac in mydict:
                stack.append(brac)
            else:
                if not stack:
                    return False    
                if not brac == mydict[stack.pop()]:
                     return False

        return len(stack) == 0 