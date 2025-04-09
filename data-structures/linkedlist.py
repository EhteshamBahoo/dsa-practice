class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
    
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

if __name__ == "__main__":
    ll = LinkedList()
    
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    
    print("Linked List:", ll.display())
    
    ll.delete(20)
    print("Linked List after deleting 20:", ll.display())
    
    ll.delete(5)
    print("Linked List after deleting 5:", ll.display())
    
    print("Is the linked list empty?", ll.is_empty())
