# cook your dish here
# cook your dish here
class Node:
    def __init__(self,data):
        self.data=data;
        self.right=None
        self.left=None
        
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
        newNode.right=self.head
        if self.head!=None:
            self.head.left=newNode
        self.head=newNode
        
        
    def getLast(self):
        x=self.head
        while x.right!=None:
            x=x.right
        print("last element is {0}".format(x.data))
        return x
        
class QuickSort:
    def __init__(self):
        print("quicksort class object has been created")
    
    def partition(self,low,high):
        pivot=low
        i=low
        j=low.right
        
        while j!=high.right and j!=None:
            if j.data<pivot.data:
                i=i.right
                x=j.data
                j.data=i.data
                i.data=x
            j=j.right
                
        
        x=pivot.data
        pivot.data=i.data
        i.data=x
        return i
    
    def quickSort(self,low,high):
        if high!=None and low!=high and low!=high.right:
            temp=self.partition(low,high)
            self.quickSort(low,temp.left)
            self.quickSort(temp.right,high)
    

        
    
        
linklist=LinkList()
linklist.insert(1)
linklist.insert(9)
linklist.insert(7)
linklist.insert(5)
linklist.insert(2)
linklist.insert(3)
linklist.insert(4)
# printing link list 
linklist.printList()
q=QuickSort()
q.quickSort(linklist.head,linklist.getLast())
linklist.printList()



