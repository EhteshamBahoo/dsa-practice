class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("front from empty queue")
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return self.queue

if __name__ == "__main__":
    q = Queue()
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("Queue after enqueueing elements:", q.display())
    
    print("Front element:", q.front())
    
    print("Dequeued element:", q.dequeue())
    
    print("Queue after dequeuing an element:", q.display())
    
    print("Is the queue empty?", q.is_empty())
    
    print("Size of the queue:", q.size())
