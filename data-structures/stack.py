class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack

if __name__ == "__main__":
    s = Stack()
    
    s.push(10)
    s.push(20)
    s.push(30)
    
    print("Stack after pushing elements:", s.display())
    
    print("Top element:", s.peek())
    
    print("Popped element:", s.pop())
    
    print("Stack after popping an element:", s.display())
    
    print("Is the stack empty?", s.is_empty())
    
    print("Size of the stack:", s.size())
