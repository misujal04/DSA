
class Node:
    def __init__(self, name: str, pid: int, pr: int):
        self.name = name
        self.pid = pid
        self.pr = pr
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value, pid, pr):
        new_node = Node(value, pid, pr)

        if self.front is None:
            self.front = self.rear = new_node
            return

        if new_node.pr < self.front.pr:
            new_node.next = self.front
            self.front = new_node

        else:
            temp = self.front

            while temp.next and temp.next.pr <= new_node.pr:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

            if new_node.next is None:
                self.rear = new_node

    def display(self):
        temp = self.front

        while temp:
            print("Patient Name:", temp.name,
                  "Patient ID:", temp.pid,
                  "Priority:", temp.pr)

            temp = temp.next

    def displaynext(self):
        if self.front is None:
            print("No patient in queue")
            return

        print("Next patient:", self.front.name)

    def dequeue(self):
        if self.front is None:
            print("No patient in queue")
            return

        print("Treatment done for:", self.front.name)

        self.front = self.front.next

        if self.front is None:
            self.rear = None


# Creating Queue object
p1 = Queue()

# Adding patients
p1.enqueue("Sujal", 101, 3)
p1.enqueue("Sahil", 102, 2)
p1.enqueue("Shivam", 103, 1)
p1.enqueue("Raj", 104, 3)


p1.display()

p1.displaynext()


p1.dequeue()


p1.display()
