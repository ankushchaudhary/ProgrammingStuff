# cook your dish here
def canRepresentBST(array):
    root=-1
    stack=[]
    for i in array:
        if i<root:
            print("No")
            return
        while len(stack)!=0 and i>stack[-1]:
            root=stack.pop()
        
        stack.append(i)
        
    print("Yes")

canRepresentBST([40 , 30 , 35 , 80 , 100])
canRepresentBST([40 , 30 , 35 , 20 ,  80 , 100])

