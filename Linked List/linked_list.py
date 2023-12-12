class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def RemoveNodeAtEnd(self):

        if self.head == None:
            return

        current_node = self.head
        while (current_node.next.next):
            current_node_value = current_node
            current_node = current_node.next
            return current_node_value

        current_node.next = None

    def RemoveNodeAtBegin(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def sizeOfList(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def concatenate(self, list2):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = list2.head
        else:
            self.head = list2.head

    def invert(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def Find(self, data):
        current_node = self.head
        position = 0
        if self.head.data == data:
            return 0
        if self.head is None:
            return

        while current_node.data == data:
            current_node = current_node.next
            position = position + 1
        return position

