class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return

        first = self.head
        last = self.head

        # Find the last node
        while last.next is not None:
            last = last.next

        # Swap data of first and last nodes
        first.data, last.data = last.data, first.data


# Main program
dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("Original Doubly Linked List:")
dll.display()

dll.swap_first_last()

print("After swapping first and last:")
dll.display()