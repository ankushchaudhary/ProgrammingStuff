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
        
    def reverse(self):
        node=self.head
        if node==None or node.pointer==None:
            return 
            
        temp=temp1=node
        prev=None;
        while temp1!=None:
            temp1=temp1.pointer
            temp.pointer=prev
            prev=temp
            temp=temp1;
            
        self.head=prev
        
def additionOfTwoNumber(num1,num2):
    result=LinkList()
    num1.reverse()
    num2.reverse()
    node1=num1.head
    node2=num2.head
    carry=0
    
    while node1!=None and node2!=None:
        result.insert((node1.data+node2.data)%10)
        carry=(node1.data+node2.data)//10
        node1=node1.pointer
        node2=node2.pointer
    
    while node1!=None:
        result.insert((node1.data+carry)%10)
        carry=(node1.data+carry)//10
        node1=node1.pointer
        
    while node2!=None:
        result.insert((node2.data+carry)%10)
        carry=(node2.data+carry)//10
        node2=node2.pointer
        
    result.printList()
        
    
        
number1=LinkList()
number2=LinkList()

for i in range(1,3):
    number1.insert(i)

for i in range(1,2):
    number2.insert(i)
    

number1.reverse()
number2.reverse()
number1.printList()
number2.printList()
additionOfTwoNumber(number1,number2)



