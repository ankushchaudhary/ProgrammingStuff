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
        
class PostfixEvaluation:
    
    def isOperator(self,op):
        if op=='*' or op=='/' or op=='+' or op=='-':
            return True
        else:
            return False
            
    def getResult(self,a,b,op):
        if op=='*':
            return a*b
        elif op=='/':
            return a//b
        elif op=='-':
            return a-b
        else:
            return a+b
            
    def posEvaluation(self,expression): 
        s=""
        st=Stack()
        for i in range(len(expression)):
            if self.isOperator(expression[i])==True:
                a=int(str(st.pop()))
                b=int(str(st.pop()))
                st.push(self.getResult(b,a,expression[i]))
            else:
                st.push(expression[i])
                
        print("the postfix evaluation is "+str(st.pop()))
                

expression=str("231*+9-")
obj=PostfixEvaluation()
obj.posEvaluation(expression)

