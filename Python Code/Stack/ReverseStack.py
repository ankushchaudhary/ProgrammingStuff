class Stack:

    def __init__(self):
        self.top=-1
        self.array=[]

    def push(self,ele):
        self.top+=1
        self.array.insert(self.top,ele)

    def pop(self):
        if len(self.array)==0:
            print("Stack Is Empty ")
            return
        self.top-=1
        return self.array.pop()

    def peek(self):
        return self.array[self.top]

    def isEmpty(self):
        if self.top<0:
            return True
        return False

    def reverseStack(self):
        if self.isEmpty()==True:
            return
        x=self.pop()
        self.reverseStack()
        self.insertAtEnd(x)

    def insertAtEnd(self,x):
        if self.isEmpty()==True:
            self.push(x)
            return
        y=self.pop()
        self.insertAtEnd(x)
        self.push(y)

    def printStack(self):
        print(self.array)



array=[13,7,6,12]
stack=Stack()
for i in range(len(array)):
    stack.push(array[i])
stack.printStack()
stack.reverseStack()
stack.printStack()
