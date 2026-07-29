from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()  
        self.minval = float("inf")

    def push(self, val: int) -> None:
        self.stack.append([self.minval,val])
        self.minval = min(self.minval,val)
        
    def pop(self) -> None:
        self.minval = self.stack[-1][0]
        return self.stack.pop()[1]
        
    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.minval

        
