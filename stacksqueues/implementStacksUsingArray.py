class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=[None]*capacity
        self.top=-1

    def is_empty(self):
        return self.top==-1
    
    def is_full(self):
        return self.top==self.capacity-1
    
    def push(self,item):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top+=1
        self.stack[self.top]=item
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item=self.stack[self.top]
        self.stack[self.top]=None
        self.top-=1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]
    
    def size(self):
        return self.top+1
    
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        return "Stack: "+str(self.stack[:self.top+1])

stack=Stack(5)
stack.push(10)
print(stack)