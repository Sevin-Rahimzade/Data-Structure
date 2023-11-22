class stack:
    top = -1
    stack = list()

    def __init__(self, size):
        for i in range(size):
            self.stack.append(None)
            self.size = size














            
    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        if self.top == self.size:
            return True
            
    def is_empty(self):
        if self.top == -1:
            return True
            
# Test :
obj = stack(5)
obj.push(2)
obj.push(4)
obj.push(3)
print(obj.stack)

print(obj.pop()) # Output : 3
print(obj.stack)

print(obj.peek()) # Output : 4