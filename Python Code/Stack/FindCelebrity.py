# cook your dish here
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
        
def hasRelation(a,b):
    if mat[a][b]==1:
        return True
    else:
        return False
        
# using 2 pointer...
def findCelebrity2(n):
    a=0
    b=n-1
    
    while(a<b):
        if hasRelation(a,b)==True:
            a+=1
        else:
            b-=1
            
    for i in range(n):
        if i!=a and (hasRelation(a,i) or not hasRelation(i,a)):
            print("there is no celebrity")
            return -1
            
    print("celebrity is {0}".format(a))
            
            
# using stack.....
def findCelebrity(n):
    stack=[]
    # pushing all celebrity in stack...
    for i in range(n):
        stack.append(i)
    
    while len(stack)!=1:
        a=stack.pop()
        b=stack.pop()
        if hasRelation(a,b)==True:
            stack.append(b)
        else:
            stack.append(a)
    
    c=stack.pop()
    
    for i in range(n):
        if i!=c and (hasRelation(c,i) or not hasRelation(i,c)):
            print("there is no celebrity")
            return -1
            
    print("celebrity is {0}".format(c))
        
        
            
mat=[[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
findCelebrity(4)
findCelebrity2(4)
        
            
    

