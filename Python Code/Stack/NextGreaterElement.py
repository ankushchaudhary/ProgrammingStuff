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

def printNextGreaterElement(array):
    stack=Stack()
    
    stack.push(array[0])
    for i in range(1,len(array)):
        maxElement=array[i]
        if maxElement>stack.peek():
            print("{0} --> {1}".format(stack.pop(),maxElement))
            while True:
                if stack.isEmpty()==False and stack.peek()<maxElement:
                    print("{0} --> {1}".format(stack.pop(),maxElement))
                else:
                    break
        stack.push(maxElement)
    while True:
        if stack.isEmpty()==False:
            print("{0} --> {1}".format(stack.pop(),-1))
        else:
            break
        

array=[13,7,6,12]
printNextGreaterElement(array)
