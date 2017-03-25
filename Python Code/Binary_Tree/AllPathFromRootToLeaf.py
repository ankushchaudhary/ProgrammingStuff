class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

# author -> Ankush Chaudhary...        
        
def printAllPathFromRootToLeaf(head,path,index):
    if head is None:
        return
    path[index]=head.data #adding data in list for every node
    index+=1
    if head.left is None and head.right is None: # checking if node is leaf or not
        print(path[:index])  # printing the path from list
        return
    else:
        printAllPathFromRootToLeaf(head.left,path,index) # going to left subtree
        printAllPathFromRootToLeaf(head.right,path,index) # going to right subtree
        
path=20*[0]             #        (1)
node1=Node(1)           #       /   \
node1.left=Node(2)      #     (2)   (3)    tree strucuture....
node1.right=Node(3)     #     / \
node1.left.left=Node(4) #   (4) (5)
node1.left.right=Node(5)
printAllPathFromRootToLeaf(node1,path,0)
