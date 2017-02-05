class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.right=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,x,y):
        newNode=Node(x,y)
        newNode.right=self.head
        self.head=newNode
        
    def deleteMiddleElementOfLine(self,head):
        if head==None:
            return

        temp=head.right
        if head.x==temp.x:
            temp1=None
            while temp!=None and temp.x==head.x:
                temp1=temp
                temp=temp.right
                if temp==None:
                    head.right=temp1
                    break
                if temp.x==temp1.x:
                    del temp1
                else:
                    head.right=temp1
            temp1.right=temp
            self.deleteMiddleElementOfLine(temp)
        elif head.y==temp.y:
            temp1=None
            while temp!=None and temp.y==head.y:
                temp1=temp
                temp=temp.right
                if temp==None:
                    head.right=temp1
                    break
                if temp.y==temp1.y:
                    del temp1
                else:
                    head.right=temp1
            temp1.right=temp
            self.deleteMiddleElementOfLine(temp)
        else:
            return
            

            
         

    def printList(self):
        temp=self.head
        if temp==None:
            print("LinkedList is empty")
            return
       # print("LinkedList is following")
        while temp!=None:
            if temp.right==None:
                exp=" "
            else:
                exp=" -> "
            print("("+str(temp.x)+","+str(temp.y)+") ",end=exp)
            temp=temp.right
        print("")
       # print("-------------------")

linkedlist=LinkedList()
for i in range(10,0,-1):
    if i<5:
        linkedlist.insert(i,15)
    else:
        linkedlist.insert(0,i)

linkedlist.printList()
linkedlist.deleteMiddleElementOfLine(linkedlist.head)
linkedlist.printList()
