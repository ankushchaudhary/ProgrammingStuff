class Stack:

    def __init__(self,size,n):
        self.array=[0]*size
        self.top=[-1]*n
        self.next=[ i for i in range(1,11)]
        self.next[size-1]=-1
        self.free=0
        
    def push(self,element,n):
        if self.free==-1:
            print(" Stack is already full !")
            return
        temp=self.free
        self.free=self.next[temp]
        self.next[temp]=self.top[n]
        self.top[n]=temp
        self.array[temp]=element
      

    def pop(self,n):
        if self.top[n]==-1:
            print(" Stack {0} is Empty ! ".format(n))
            return

        print("pop element from stack {0} is {1} ".format(n,self.array[self.top[n]]))
        temp=self.top[n]
        self.top[n]=self.next[temp]
        self.next[temp]=self.free
        self.free=temp

    def peek(self,n):

        if self.top[n]==-1:
            print(" Stack {0} is Empty ! ".format(n))
            return

        print(" top element of Stack {0} is {1} !".format(n,self.array[self.top[n]]))

stack=Stack(10,3)
stack.push(15,2)
stack.push(45,2)
stack.push(17,1)
stack.push(49,1)
stack.push(39,1)
stack.push(11,0)
stack.push(9,0)
stack.push(7,0)
stack.pop(2)
stack.pop(1)
stack.pop(0)
    
        
