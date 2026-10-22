class Node:
    def __init__ (self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        temp=self.top
        print("Poped Element:",temp.data)
        self.top=self.top.next
        temp=None
    def print(self):
         print("Stack contains:...")
         temp=self.top
         while temp:
            print(temp.data)
            temp=temp.next
    def reverse(self):
        temp=self.top
        while temp:
            st1.push(Node(temp.data))
            temp=temp.next
        

    



st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.pop()
st.print()
st.reverse()
st1.print()