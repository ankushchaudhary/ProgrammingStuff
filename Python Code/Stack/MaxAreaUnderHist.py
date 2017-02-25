def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False

def getMaxRectangleAreaInHistogram(array):
    stack=[]
    n=len(array)
    i=0
    area=0
    top=0
    maxArea=-1
    while i<=n:
        if i<n and (isEmpty(stack)==True or array[stack[-1]]<=array[i]):
            stack.append(i)
        else:
            while (isEmpty(stack)==False and (i==n or array[stack[-1]]>array[i])):
                top=stack.pop()
                if isEmpty(stack)==False:
                    area=array[top]*(i-stack[-1]-1)
                else:
                    area=array[top]*i
                maxArea=max(area,maxArea)
            if i<n:
                stack.append(i)
        
        i+=1
    
    
    
   
        
        
    print("max area under histogram is %s "%maxArea)
        
 
    
array=[2,1,2,3,1]
getMaxRectangleAreaInHistogram(array)
        
            
    

