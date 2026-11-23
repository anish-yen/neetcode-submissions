class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = [] #keep track of mins wiht stack
        #popping from min stack o(1) heap finds min but removing arbitrary values complicated
        #hashmap finds value but doesnt know smallest value automatically
        #stack remembers mi each pop
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.mins:#edge case
            self.mins.append(val)
        else:
            self.mins.append( min(self.mins[-1], val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop() #track mins every element current for stack
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
