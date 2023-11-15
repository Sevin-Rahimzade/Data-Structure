class Array:
    array = []

    def __init__(self, arraySize):
        for i in range(arraySize):
            self.array.append(None)
            self.size = arraySize
