class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)

head=a
a.next=b
b.next=c
c.next=d

def linklist():
    print("\n")
    current=head
    while current is not None:
        print(current.data,end=("-->"))
        current=current.next

linklist()

def insertnodestart():
    global head
    new_node=Node(0)
    new_node.next=head
    head=new_node



def insertnodelast():
    new_node2=Node(5)
    d.next=new_node2

def insertnodepostition():
    new_node3=Node(100)
    n=int(input("Enter the position on which you want to enter the node"))
    current=head
    for i in range(n-1):
        while head is not None:
            print(current.data,end="-->")
            current=current.next
    current.next=new_node3
    print(current.data,end="-->")
    current=current.next
insertnodepostition()