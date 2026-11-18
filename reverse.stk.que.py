#Reversing a queue using stack
#Reversing a stack using queue

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("empty")
        else:
            temp =self.top
            popped_data = temp.data
            #print("Popped", temp.data)
            self.top = self.top.next
            temp = None
        return popped_data

    def display(self):
            if self.isempty():
                print("empty")
            else:
                print("stack contains..")
                temp = self.top
                while temp:
                    print(temp.data)
                    temp = temp.next


class queue:
    def __init__(self):
        self.fro = self.rear = None

    def isempty(self):
        return self.fro is None
    
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.fro = self.rear = new_node

    def dequeue(self):
        temp = self.fro
        dqued_data= temp.data
        self.fro = self.fro.next
        
        if self.fro == None:
            print("EMpty")
            self.rear = None
        temp = None
        return dqued_data

    def print(self):
        temp = self.fro
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

def reverse_stack(s1):
    q1 = queue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))
    q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.display()



# q= queue()
# q.enqueue(Node(10))
# q.enqueue(Node(21))
# q.enqueue(Node(37))
# q.enqueue(Node(49))
# q.print()


st = stack()
st.push(Node(5))
st.push(Node(15))
st.push(Node(25))
st.push(Node(35))
st.display()
q=queue()
reverse_stack(st)
