# cook your dish here
class TwoStack:
    def __init__(self,size):
        self.top1=-1
        self.stack=[0 for i in range(size-2)]
        self.top2=size
        self.size=size
        
        
    def isEmpty(self):
        if self.top==-1 and self.top2==self.size:
            return True
        return False
        
    def push1(self,n):
        self.top1+=1
        self.stack.insert(self.top1,n)
        
    def pop1(self):
        if self.top1==-1:
            print("stack1 is already empty")
            return
        x=self.stack[self.top1]
        self.stack[self.top1]=0
        self.top1-=1;
        return x
        
    def push2(self,n):
        self.top2-=1
        self.stack.insert(self.top2,n)
        
    def pop2(self):
        if self.top2==self.size:
            print("stack2 is already empty")
            return
        x=self.stack[self.top2]
        self.stack[self.top2]=0
        self.top+=1;
        return x
        
    def printStack(self):
        print(self.stack)
        
    
        
    
obj=TwoStack(10)
obj.pop1()
obj.push1(1)
obj.pop2()
obj.push2(2)
obj.pop1()
obj.printStack()
