class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_occurrences(head, key):
    count = 0
    current = head

    while current is not None:
        if current.data == key:
            count += 1
        current = current.next

    return count

# Creating a linked list: 10 -> 20 -> 10 -> 30 -> 10
head = Node(10)
head.next = Node(20)
head.next.next = Node(10)
head.next.next.next = Node(30)
head.next.next.next.next = Node(10)

key = 10
print("Occurrences:", count_occurrences(head, key))