# cook your dish here
class Node:
    def __init__(self,data):
        self.data=data;
        self.right=None;
        self.down=None;
        
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
            node=node.right
        print("")    
        print("--------------------")
        
    def insert(self,x):
        newNode=Node(x)
        newNode.pointer=self.head
        self.head=newNode
        
    def merge(self,a,b):
        if a==None:
            return b
        
        if b==None:
            return a
        
        temp=None
        
        if a.data<=b.data:
            temp=a
            temp.right=self.merge(a.right,b)
        else:
            temp=b
            temp.right=self.merge(a,b.right)
        
        return temp
        
    def flatten(self,node):
        if node==None :
            return node
        
        node.right=self.flatten(node.right)
        node.down=self.flatten(node.down)
        node.right=self.merge(node.right,node.down)
        node.down=None
        return node
        
        
    
        
linklist=LinkList()
linklist.head=Node(5)
linklist.head.right=Node(10)
linklist.head.right.right=Node(20)
linklist.head.down=Node(6)
linklist.head.right.down=Node(11)
linklist.head=linklist.flatten(linklist.head)
linklist.printList()

