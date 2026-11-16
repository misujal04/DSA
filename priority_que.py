class Node:
    def __init__(self,value,pr):
        self.data=value
        self.pr=pr                              #pr is priority here
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.front==None:
            self.front=new_node
            return
        if self.front.pr>new_node.pr:
           # self.front=new_node
            new_node.next=self.front
            self.front=new_node
            return
        else:
            temp=self.front
            #prev=None
            while temp:#here was temp.next
                if new_node.pr<temp.pr:
                    break
                else:   
                    prev=temp
                    temp=temp.next
            prev.next=new_node
            new_node.next=temp

    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

pq=PriorityQueue()
pq.enqueue(Node(100,2))
pq.enqueue(Node(500,6))
pq.enqueue(Node(100,2))
pq.display()

