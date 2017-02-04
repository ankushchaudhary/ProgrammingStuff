# cook your dish here
class Node:
    def __init__(self,data):
        self.data=data;
        self.pointer=None;
        
class LinkList:
    def __init__(self):
        self.head=None;
    
    def printList(self,node):
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
        
    def reverseAlternateInGroupOfK(self,node,k):
        if node==None or node.pointer==None:
            return node
            
        temp=temp1=node
        prev=None;
        count=0
        while temp1!=None and count!=k:
            temp1=temp1.pointer
            temp.pointer=prev
            prev=temp
            temp=temp1;
            count+=1
        
        count=0
        while temp1!=None and count!=k:
            node.pointer=temp1
            temp1=temp1.pointer
            node=node.pointer
            count+=1
        
        if temp1==None:
            return prev
        
        node.pointer=self.reverseAlternateInGroupOfK(temp1,k)
        return prev
        
        
linklist=LinkList()
for i in range(12):
    linklist.insert(i)
linklist.printList(linklist.head)
linklist.printList(linklist.reverseAlternateInGroupOfK(linklist.head,4))


