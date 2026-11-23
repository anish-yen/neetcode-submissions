class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.mins:#edge case
            self.mins.append(val)

        self.mins.append( min(self.mins[-1], val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop() #track mins every element current for stack
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
