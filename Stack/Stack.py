class stack:
    top = -1
    stack = list()

    def __init__(self, size):
        for i in range(size):
            self.stack.append(None)
            self.size = size

