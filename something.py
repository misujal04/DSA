# * doubly linear linked list create, print, insert, delete 

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None

class Doubly_LLL:
    def __init__(self):
        self.head=None

    def append(self,newnode):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp  
        else:
            self.head=newnode  #? if the list is empty add the firt node

    def print(self):
        temp=self.head
        while temp:
            # * my code
            prev_val = temp.prev.data if temp.prev else None
            next_val = temp.next.data if temp.next else None
            print(f"Prev: {prev_val} | Data: {temp.data} | Next: {next_val}")
            temp=temp.next
        print()


    def insert(self, newnode,pos): #? 4 links are required but for the last node u need 3 links
        temp=self.head
        if pos==1:
            newnode.next=self.head

            if self.head:
                self.head.prev=newnode
            self.head=newnode
        else:
            p=1
            while(p<pos-1):  
                temp=temp.next
                p+=1

            newnode.prev=temp
            newnode.next=temp.next

            if temp.next:  #? last node 3 links
                    temp.next.prev=newnode
            temp.next=newnode

    def delete(self,value):
        temp=self.head
        if temp.data==value:
            self.head=self.head.next
            self.head.prev=None

        else:
            while temp.data!=value and temp:
                temp=temp.next
                if temp==None:
                    print("value not in the list")
                    print()
                    return
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.prev
            temp=None



list= Doubly_LLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)
list.append(Node(60))

list.print()

# list.insert(Node(25),7)
# list.print()

list.delete(670)
list.print()