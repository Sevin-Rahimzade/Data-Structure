class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)] 
        self.front = self.rear = -1


    def isempty(self):
        if self.front == -1:
            return True
        
    def isfull(self):
        if ((self.front == 0 and self.rear == -1) or ((self.rear+1) % self.size == self.front )):
            return True

    def peekQueue(self):
        return self.queue[self.front]