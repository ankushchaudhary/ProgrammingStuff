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
        
     def reverseInGroup(self,node,k):
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
            
        node.pointer=self.reverseInGroup(temp,k)
        return prev
        
        
linklist=LinkList()
for i in range(12):
    linklist.insert(i)
linklist.printList(linklist.head)
linklist.printList(linklist.reverseInGroup(linklist.head,4))


