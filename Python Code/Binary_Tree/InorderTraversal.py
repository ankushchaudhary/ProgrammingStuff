# Inorder travesal without stack and without recursion
# Time complexity-O(n) and Space complexity-O(1)
# Author -> Ankush Chaudhary...

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

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
        
    def inorderTraversalWithoutRecursionAndWithoutStack(self):
        current=self.head
        
        while current is not None:
                 
            if current.left is None:
                print(" %d "%current.data,end=' ')
                current=current.right
            else:
                pre=current.left
                while pre.right is not None and pre.right is not current:
                    pre=pre.right
                
                if pre.right is None:
                    pre.right=current
                    current=current.left
                else:
                    print("%d "%current.data, end=' ')
                    pre.right=None
                    current=current.right
     
    def inorderTraversal(self,head):
        if head is None:
            return
        self.inorderTraversal(head.left)
        print("%d "%head.data,end=' ')
        self.inorderTraversal(head.right)
            
        
        
             #        (4)
             #       /   \
             #     (2)   (7)    tree strucuture....
             #     / \
             #   (1) (3)        
        
        


bt=BinaryTree()
bt.head=bt.insert(4,bt.head)
bt.head=bt.insert(2,bt.head)
bt.head=bt.insert(3,bt.head)
bt.head=bt.insert(1,bt.head)
bt.head=bt.insert(7,bt.head)
bt.inorderTraversal(bt.head)
print()
bt.inorderTraversalWithoutRecursionAndWithoutStack()
print()
