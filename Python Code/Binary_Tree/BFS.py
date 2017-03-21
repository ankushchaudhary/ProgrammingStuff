# cook your dish here
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.head=None
    
    def insert(self,data,head):
        if head==None:
            head=Node(data)
            return head
        
        if head.data>=data:
            head.left=self.insert(data,head.left)
            
        else:
            head.right=self.insert(data,head.right)
            
        return head
        
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
            print("%d "%head.data,end=' ')
            return
        self.printLevel(k-1,head.left)
        self.printLevel(k-1,head.right)
        
    def printAllLevel1(self):
        height=self.getHeight(self.head)
        for i in range(height):
            self.printLevel(i,self.head)
            print("")
            
    def printAllLevel2(self):
        lst=[]
        temp=self.head
        lst.append(temp)
        count=1
        while True:
            count=len(lst)
            if count<=0:
                break;
            
            while count>0:
                tem=lst.pop(0)
                print("%d"%tem.data,end=' ')
                count-=1
                if tem.left!=None:
                    lst.append(tem.left)
                
                if tem.right!=None:
                    lst.append(tem.right)
                    
            print("")
            
            
            
bt=BinaryTree()
bt.head=bt.insert(4,bt.head)
bt.head=bt.insert(2,bt.head)
bt.head=bt.insert(6,bt.head)
bt.head=bt.insert(1,bt.head)
bt.head=bt.insert(3,bt.head)
bt.head=bt.insert(5,bt.head)
bt.head=bt.insert(7,bt.head)
bt.printAllLevel1()
bt.printAllLevel2()
        
        
        
    

