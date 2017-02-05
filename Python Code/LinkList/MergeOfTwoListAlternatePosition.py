class Node:
    def __init__(self,element):
        self.right=None
        self.element=element

class LinkList:
    def insert(self,element):
        newNode=Node(element)
        newNode.right=self.head
        self.head=newNode

    def __init__(self):
        self.head=None

    def printList(self):
        if self.head==None:
            print("linklist is empty")
            return
        node=self.head
        while node!=None:
            print(str(node.element),end=' ')
            node=node.right
        print("")

    def mergeAlternate(self,head2):
        node=self.head
        while head2!=None:
            temp=node.right
            node.right=head2
            head2=head2.right
            if node==None or node.right==None:
                return
            node.right.right=temp
            node=node.right.right
            


link1=LinkList()
link2=LinkList()

for i in range(10,0,-1):
    if i%2==1:
        link1.insert(i)
    else:
        link2.insert(i)

link1.printList()
link2.printList()
#calling mergeAlternate for merging both linklist
link1.mergeAlternate(link2.head)
#printing the merge linklist
link1.printList()


