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

    def isMatch(self,b,a):
        if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}'):
            return True
        return False

    def isOpener(self,a):
        if a=='(' or a=='{' or a=='[':
            return True
        #print("false: opener")
        return False

    def checkBalancedParenthesis(self,exp):
        for i in range(len(exp)):
            
            if self.isOpener(exp[i])==True:
                self.push(exp[i])
            else:
                if self.isEmpty()==False and self.isMatch(exp[i],self.peek())==True:
                    self.pop()
                else:
                    print("Not Balanced1 !")
                    return
            print(self.array)
            
        if self.isEmpty()==False:
            print("Not Balanced !")
            return
        print("Balanced !")

stack=Stack()
exp="[()]{}{[()()]}"
stack.checkBalancedParenthesis(exp)
exp="[(])"
stack.checkBalancedParenthesis(exp)
