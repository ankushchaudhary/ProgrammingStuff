def findMaxLen(expression):
    stack=[-1]
    length=0
    for i in range(len(expression)):
        if expression[i]=='(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack)!=0:
                length=max(length,i-stack[len(stack)-1])
            else:
                stack.append(i)
    
    print("maximum length of valid expression is {0}".format(length))
    
    
array=["((()()","()(()))))"]
for i in range(len(array)):
    findMaxLen(array[i])
