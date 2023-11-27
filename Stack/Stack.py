class stack:
    top = -1
    stack = list()

    def __init__(self, size):
        for i in range(size):
            self.stack.append(None)
            self.size = size

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            element = self.items[-1]
            del self.items[-1]
            return element
        else:
            raise Exception("Stack is empty")
            
    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        if self.top == self.size:
            return True
            
    def is_empty(self):
        if self.top == -1:
            return True
            
