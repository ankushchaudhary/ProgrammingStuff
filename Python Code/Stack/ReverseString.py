# cook your dish here
class Stack:
    def __init__(self):
        self.top=-1
        self.stack=[]
        
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
        
    def push(self,n):
        self.top+=1
        self.stack.insert(self.top,n)
        
    def pop(self):
        if self.top==-1:
            return "stack is already empty"
        self.top-=1;
        return self.stack.pop()
        
    def printStack(self):
        print(self.stack)
        
    def peek(self):
        return self.stack[self.top]
        
    def reverse(self,exp):
        
        for i in range(len(exp)):
            self.push(exp[i])
        
        revExp=""
        while self.isEmpty()!=True:
            revExp+=self.pop()
        
        print('reverse of "{0}" is "{1}" '.format(exp,revExp))
        

st=Stack()
st.reverse("hello ! how you doing")
