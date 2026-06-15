class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefix:
            if self.prefix[-1] < val:
                self.prefix.append(self.prefix[-1])
                #self.stack.append(val)
            else: # if val < prefix top
                #self.stack.append(val)
                self.prefix.append(val)
        else:
            self.prefix.append(val)


    def pop(self) -> None:
        self.stack.pop()
        if self.prefix:
            self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1]
