class Array:
    array = []

    def __init__(self, arraySize):
        for i in range(arraySize):
            self.array.append(None)
            self.size = arraySize

    def Insert(self, object, index):
        if index < self.size:
            self.array[index] = object
            return index
        else:
            return -1

    def Delete(self, index):
        if index < self.size:
            obj = self.array[index]
            self.array[index] = None
            return obj
        else:
            return None
