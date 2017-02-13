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
        
def maximumSumLinkdedListWithTwoSortedListCommonNode(node1,node2):
    pre1=node1
    pre2=node2
    curr1=node1
    curr2=node2
    while curr1!=None and curr2!=None:
        sum1=sum2=0
        while curr1!=None and curr2!=None and curr1.data!=curr2.data:
            if curr1.data > curr2.data:
                sum1+=curr1.data
                curr1=curr1.pointer
            else:
                sum2+=curr2.data
                curr2=curr2.pointer

        if pre1==node1 and pre2==node2:
            if sum1>sum2:
                



        
        
    
        
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



