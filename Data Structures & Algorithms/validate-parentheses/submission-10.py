class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"{" : "}", "(":")", "[" : "]"}

        for c in s:
            if c in mydict:
                stack.append(c)
            else:
                if not stack:
                    return False
                if not c == mydict[stack.pop()]:
                    return False

                
        return len(stack) == 0


