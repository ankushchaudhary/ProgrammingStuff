# cook your dish here
class Node:
    
    def __init__(self,data):
        self.data=data
        self.right=None
        self.arbit=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def printList(self):
        temp=self.head
        while temp!=None:
            print(str(temp.data),end=" ")
            temp=temp.right
        print("")
        
    def printList(self,node):
        temp=node
        while temp!=None:
            print(str(temp.data),end=" ")
            temp=temp.right
        print("")
    
    def insert(self,data):
        newNode=Node(data)
        newNode.right=self.head
        self.head=newNode
    
    def cloneLinkedListWithNextAndArbitPointerUtil(self):
        temp=self.head
        while temp!=None:
            newNode=Node(temp.data)
            newNode.right=temp.right
            temp.right=newNode
            temp=newNode.right
            
        
    def cloneLinkedListWithNextAndArbitPointer(self):
        self.cloneLinkedListWithNextAndArbitPointerUtil()
        temp=self.head
        node2=temp1=temp.right
        while temp!=None:
            temp1.arbit=temp.arbit.right
            temp.right=temp1.right
            if temp1==None or temp==None or temp1.right==None or temp.right==None:
                break
            temp1.right=temp.right.right
           
            temp1=temp1.right
            temp=temp.right
        self.printList(node2)
    
    def insertElement(self):
        newNode1=Node(1)
        newNode2=Node(2)
        newNode3=Node(3)
        newNode4=Node(4)
        self.head=newNode1
        newNode1.right=newNode2
        newNode2.right=newNode3
        newNode3.right=newNode4
        newNode1.arbit=newNode3
        newNode2.arbit=newNode3
        newNode3.arbit=newNode4
        newNode4.arbit=newNode3
        

ll=LinkedList()
ll.insertElement()
ll.printList(ll.head)
ll.cloneLinkedListWithNextAndArbitPointer()
            
