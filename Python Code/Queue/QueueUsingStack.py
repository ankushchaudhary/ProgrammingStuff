class Stack:    #this class is just for stack object
    
    def __init__(self):
        self.array=[]
    
    def isEmpty(self):  #simple function for checking wether stack is empty or not
        
        if(len(self.array)==0):
            return True
        
        return False
        
    def push(self,element):   #this is just for pushing an element in Stack
        self.array.append(element)
       # print(self.array)
        
    def pop(self):          #just for popping element from Stack
        if self.isEmpty()==True:
            print("stack is already Empty")
            return
        
        return self.array.pop()
            
    def peek(self):
        return self.array[-1]
        
class QueueUsingStack:   # in this class we are implementing the main logic
    
    def __init__(self): # inside constructor just creating two stack
        self.stack1=Stack()
        self.stack2=Stack()
    
    def enqueue(self,element): #in enqueue , we are just simply enqueuing element in Stack1
        print("Enqueuing %d in Queue"%element)
        self.stack1.push(element)
      #  print(self.stack1.array)
        
        
    def dequeue(self): 
        if self.stack1.isEmpty()==True and self.stack2.isEmpty()==True: #here we are checking wether an element exists in either of stack
            print("Queue is Already Empty") # if not then , there is no element to dequeue
            return -1
        
        if self.stack2.isEmpty()==True:  # just checking whether stack2 is empty or not
            while self.stack1.isEmpty()==False: # if true, then pushing all element of stack1 into stack2
                self.stack2.push(self.stack1.pop())
            
        return self.stack2.pop()  # popping top element of stack2 and returning
        
queue=QueueUsingStack() 
queue.enqueue(1)
queue.enqueue(2)
print("Dequeuing {0} from Queue ".format(queue.dequeue()))
print("Dequeuing {0} from Queue ".format(queue.dequeue()))
print("Dequeuing {0} from Queue ".format(queue.dequeue()))
        

    
