# cook your dish here
def moveDiskBetweenStack(src,des,s,d):
    len1=len(src)
    len2=len(des)
    if len1==0:
        src.append(des.pop())
        print("move disk {0} from {1} to {2}".format(src[0],d,s))
        return
    if len2==0:
        des.append(src.pop())
        print("move disk {0} from {1} to {2}".format(des[0],s,d))
        return
    
    a=src.pop()
    b=des.pop()
    if a>b :
        src.append(a)
        src.append(b)
        print("move disk {0} from {1} to {2}".format(b,d,s))
    else:
        des.append(b)
        des.append(a)
        print("move disk {0} from {1} to {2}".format(a,s,d))
        

       
    
    
    
def towerOfHanoiIterative(n):
    src,aux,des=[],[],[];
    for i in range(n,0,-1):
        src.append(i)
    print(src)
    print(aux)
    print(des)
    
    for i in range(1,pow(2,n)):
        if i%3==1:
            moveDiskBetweenStack(src,des,'S','D')
        elif i%3==2:
            moveDiskBetweenStack(src,aux,'S','A')
        else:
            moveDiskBetweenStack(aux,des,'A','D')

towerOfHanoiIterative(3)
    
