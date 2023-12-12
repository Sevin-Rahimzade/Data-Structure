class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def RemoveAtEnd(self):
        new_node = self.head
        if self.head is Node:
            return False
        while new_node.next.next != None:
            new_node = new_node.next
        new_node.next = None
        new_node.perv = new_node

    def RemoveNodeAtBegin(self):
        if self.head is None:
            raise Exception("The list is Empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def SizeOfList(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def Concatenate(self, other_list):
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head
        if other_list.head:
            other_list.head.prev = current

    def Invert(self):
        current = None
        temp = self.head
        while temp:
            current = temp
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        if current:
            self.head = current