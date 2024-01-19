class stack:
    top = -1
    stack = list()

    def __init__(self, size):
        self.stack = [None] * size
        self.size = size

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = item
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            element = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return element 
        else:
            raise Exception("Stack is empty")
            
    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        if self.top == self.size -1:
            return True
            
    def is_empty(self):
        if self.top == -1:
            return True
        
