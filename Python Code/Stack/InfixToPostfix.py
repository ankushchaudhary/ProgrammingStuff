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
        
class InfixToPostfix:
    
    def __init__(self):
        self.precedence={'+':1,'-':1,'*':2,'/':2}
    
    def getPrecedence(self,op):
        return self.precedence[op]
    
    def isOperator(self,op):
        if op=='(' or op==')' or op=='*' or op=='/' or op=='+' or op=='-':
            return True
        else:
            return False
            
    def inToPos(self,expression): 
        s=""
        st=Stack()
        for i in range(len(expression)):
            if self.isOperator(expression[i])==True:
                if expression[i]==')':
                    while True:
                        temp=st.pop()
                        if temp=='(':
                            break
                        s+=temp
                elif expression[i]=='(':
                    st.push(expression[i])
                else:
                    while st.isEmpty()!=True and st.peek()!='(' and self.getPrecedence(expression[i])<=self.getPrecedence(st.peek()):
                        s+=st.pop()
                    st.push(expression[i])
                    
            else:
                s+=expression[i]
        while st.isEmpty()!=True:
            s+=st.pop()
                
        print("the infix to postfix is "+s)
                

expression="a+b+c+d"
obj=InfixToPostfix()
obj.inToPos(expression)

