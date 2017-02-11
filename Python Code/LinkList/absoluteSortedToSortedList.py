# cook your dish here
class Node:
    
    def __init__(self,data):
        self.data=data
        self.right=None
        
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
        
    def printList(self):
        temp=self.head
        while temp!=None:
            print(str(temp.data),end=" ")
            temp=temp.right
        print("")
    
    def insert(self,data):
        newNode=Node(data)
        newNode.right=self.head
        self.head=newNode
    
    
    def sortList(self):
       prev=self.head
       current=prev.right
       while current!=None:
            
            if current.data<0:
               prev.right=current.right
               current.right=self.head
               self.head=current
               current=prev.right
            else:
                prev=current
                current=current.right
        
   
ll=LinkedList()
ll.insert(-5)
ll.insert(-4)
ll.insert(-3)
ll.insert(-2)
ll.insert(-1)
ll.printList()
ll.sortList()
ll.printList()

