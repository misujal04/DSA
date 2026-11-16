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



def insertnodestart():
    global head
    new_node=Node(0)
    new_node.next=head
    head=new_node



def insertnodelast():
    new_node2=Node(5)
    current=head
    while current is not None:
        print(current.data)
        temp=current
        current=current.next
    temp.next=new_node2
    
def insertnodepostition():
    new_node3=Node(100)
    n=int(input("Enter the position on which you want to enter the node"))
    current=head
    for i in range(n):
        while current is not None:
            current=current.next
    current.next=new_node3
    new_node3.next=current.next.next

#linklist()
insertnodelast()
linklist()

# n=int(input("Enter the position on which you want to enter the node"))
# current=head
# for i in range(n-1):
#     while current is not None:
#         current=current.next
# current