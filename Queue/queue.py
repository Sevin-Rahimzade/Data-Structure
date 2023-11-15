class QueueReplica:
    counter = -1
    queue = list()

    def __init__(self, size):
        for i in range(size):
            self.queue.append(None)
            self.size = size

    def enqueue(self, value):
        if(self.counter == -1):
            self.counter += 1
            self.queue[self.counter] = value
        elif self.counter == self.size:
            self.is_full()
        else:
            self.counter += 1
            self.queue[self.counter] = value


    def dequeue(self):
        if self.counter != -1:
            for i in range(self.size - 1):
                self.queue[i] = self.queue[i + 1]
        else:
            self.is_empty()

    def peek(self):
        return self.queue[0]
    
    

    def is_empty(self):
        if self.counter == -1:
            return True
        else:
            return False


    def is_full(self):
        if self.counter == self.size:
            return True
        else:
            return False

    def reverse(self):
        return self.queue[::-1]



# test
obj = QueueReplica(5)
obj.enqueue(2)
obj.enqueue(4)
obj.enqueue(3)
print(obj.queue)

obj.dequeue()
print(obj.queue)

print(obj.peek())
