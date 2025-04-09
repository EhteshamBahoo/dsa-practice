class Deque:
    def __init__(self):
        self.deque = []
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def add_first(self, item):
        self.deque.insert(0, item)
    
    def add_last(self, item):
        self.deque.append(item)
    
    def remove_first(self):
        if not self.is_empty():
            return self.deque.pop(0)
        else:
            raise IndexError("remove_first from empty deque")
    
    def remove_last(self):
        if not self.is_empty():
            return self.deque.pop()
        else:
            raise IndexError("remove_last from empty deque")
    
    def front(self):
        if not self.is_empty():
            return self.deque[0]
        else:
            raise IndexError("front from empty deque")
    
    def rear(self):
        if not self.is_empty():
            return self.deque[-1]
        else:
            raise IndexError("rear from empty deque")
    
    def size(self):
        return len(self.deque)
    
    def display(self):
        return self.deque

if __name__ == "__main__":
    d = Deque()
    
    d.add_last(10)
    d.add_last(20)
    d.add_first(5)
    
    print("Deque after adding elements:", d.display())
    
    print("Front element:", d.front())
    
    print("Rear element:", d.rear())
    
    print("Removed from front:", d.remove_first())
    
    print("Removed from rear:", d.remove_last())
    
    print("Deque after removals:", d.display())
    
    print("Is the deque empty?", d.is_empty())
    
    print("Size of the deque:", d.size())
