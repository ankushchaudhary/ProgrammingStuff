class Node:# cook your dish here
class Node:
    
    def __init__(self,x):
        self.data=x
        self.right=None
        self.left=None
        
class Stack:
    
    def __init__(self):
        self.top=None
        self.mid=None
        self.count=0
        
    def isEmpty(self):
        if self.top==None:
            return True
        return False
        
    def peek(self):
        return self.top.data
        
    def pop(self):
        if self.top==None:
            print(" Stack is empty !")
            return
        
        
        data=self.top.data
        node=self.top
        self.top=self.top.right
        if self.top!=None:
            self.top.left=None
        self.count-=1
        if self.count%2==0:
            self.mid=self.mid.right
        del node
        return data
        
    def getMiddle(self):
        if self.isEmpty()==True:
            print(" Stack is empty !")
            return
            
        print("middle of stack is {0}".format(self.mid.data))
        
    def push(self,x):
        self.count+=1
        
        newNode=Node(x)
        
        if self.count==1:
            self.top=newNode
            self.mid=self.top
            return
        
        
        
        newNode.right=self.top
        self.top.left=newNode
        self.top=newNode
        
        
        
        if self.count%2==1:
            self.mid=self.mid.left


st=Stack()
for i in range(9):
    st.push(i)
    st.getMiddle()

for i in range(9):
    st.pop()
    st.getMiddle()

