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
        
    def sortedInsert(self,node,sort):
        if sort==None:
            return node
            
        if sort.data>node.data:
            node.right=sort
            return node
            
        temp1=sort
        while temp1.right!=None and temp1.right.data<node.data:
            temp1=temp1.right
        
        if temp1.right==None:
            temp1.right=node
            return sort
            
        node.right=temp1.right
        temp1.right=node
        return sort
        
        
    def insertionSort(self):
        current=self.head
        sort=None
        while current!=None:
            temp=current.right
            current.right=None
            sort=self.sortedInsert(current,sort)
            current=temp
        self.head=sort
            
            
        

ll=LinkedList()

for i in range(1,10,2):
    ll.insert(i)
ll.printList()
ll.insertionSort()
ll.printList()

