class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)
        
    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                last_element1 = self.enqueue_stack[-1]
                del self.enqueue_stack[-1]
                self.dequeue_stack.append(last_element1)
        if self.dequeue_stack:
            last_element2 = self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return last_element2
        else:
            raise IndexError("Queue is empty")


# Test :
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output : 1
print(q.dequeue())  # Output : 2
print(q.dequeue())  # Output : 3