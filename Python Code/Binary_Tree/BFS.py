# cook your dish here
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        if self.head==None:
            self.head=Node(data)
            return self.head
        
        if self.head.data>=data:
            self.head.left=self.insert(self.head.left,data)
            
        else:
            self.head.right=self.insert(self.head.right,data)
            
        return self.head
        
    def getHeight(self,head):
        if self==None:
            return 0
        if head.left==None and head.right==None:
            return 1
        lh=self.getHeight(head.left)
        rh=self.getHeight(head.right)
        return 1+max(lh,rh);
        
    def printLevel(self,k,head):
        if k==0:
            print("%d "%head.data)
            return
        self.printLevel(k-1,head.left)
        self.printLevel(k-1,head.right)
        
    def printAllLevel(self):
        height=self.getHeight(self.head)
        for i in range(height):
            printLevel(i,self.head)
            
bt=BinaryTree()
bt.insert(4)
bt.insert(2)
bt.insert(6)
bt.insert(1)
bt.insert(3)
bt.insert(5)
bt.insert(7)
bt.printAllLevel()
        
        
        
    

