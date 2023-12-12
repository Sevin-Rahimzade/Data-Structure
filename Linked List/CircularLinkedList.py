class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def RmeoveAtEnd(self):
        if self.head == None:
            return False
        elif self.head.next == self.head:
            self.head = None
        new_node = self.head
        while new_node.next.next != self.head:
            new_node = new_node.next
        new_node.next = self.head

    def RemoveNodeAtBegin(self):
        if self.head is None:
            return None
        temp = self.head
        data = temp.data
        if self.head.next == self.head:
            self.head = None
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        return data

    def SizeOfList(self):
        if self.head is None:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            current = current.next
            count += 1
        return count

    def Concatenate(self, other_linked_list):
        if self.head is None:
            self.head = other_linked_list.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = other_linked_list.head

    def Invert(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        next_node = self.head.next
        while next_node != self.head:
            current.next = prev
            prev = current
            current = next_node
            next_node = next_node.next
        current.next = prev
        self.head.next = current
        self.head = current
