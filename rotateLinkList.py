# cook your dish here
class Node:
    def __init__(self,data):
        self.data=data;
        self.pointer=None;
        
class LinkList:
    def __init__(self):
        self.head=None;
    
    def printList(self):
        node=self.head
        if node==None:
            print("linklist is empty")
            return
        
        print("linklist is following")
        print("--------------------")
        while node!=None:
            print(str(node.data),end=" ")
            node=node.pointer
        print("")    
        print("--------------------")
        
    def insert(self,x):
        newNode=Node(x)
        newNode.pointer=self.head
        self.head=newNode
        
    def rotate(self,k):
        node=self.head
        count=0
        temp=None
        
        while count!=k:
            temp=node
            node=node.pointer
            count+=1
        
        while node.pointer!=None:
            node=node.pointer
        
        temp1=self.head
        self.head=temp.pointer
        temp.pointer=None
        node.pointer=temp1
        
        
        
    
        
linklist=LinkList()

for i in range(10,0,-1):
    linklist.insert(i)
linklist.printList()
linklist.rotate(5)
linklist.printList()

