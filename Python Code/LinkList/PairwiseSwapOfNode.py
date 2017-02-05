class Node:
    def __init__(self,x):
        self.data=x
        self.right=None

class LinkedList:
    def __init__(self):
        self.head=None
        count=0

    def insert(self,x):
        newNode=Node(x)
        newNode.right=self.head
        self.head=newNode

    def pairwiseSwap(self,temp):
        if temp==None or temp.right==None:
            return temp

        tmp1=temp.right
        node=tmp1.right
        tmp1.right=temp
        temp.right=self.pairwiseSwap(node)
        return tmp1
         

    def printList(self):
        temp=self.head
        if temp==None:
            print("LinkedList is empty")
            return
       # print("LinkedList is following")
        string=""
        while temp!=None:
            string+=str(temp.data)+" "
            temp=temp.right
        print(string)
       # print("-------------------")

linkedlist=LinkedList()
for i in range(1,10):
    linkedlist.insert(i)

print("linked list before pairwise swap")
linkedlist.printList()
linkedlist.head=linkedlist.pairwiseSwap(linkedlist.head)
linkedlist.printList()
