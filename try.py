class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)

head=a
a.next=b
b.next=c

current=head
while current!=None:
    print(current.data,end="-->")
    current=current.next
print(None)
