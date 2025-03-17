class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0  
        print("Created new LinkedList")
        print(f"Current size: {self.size}")
        print("Head: None")

    def append(self, element):
        new_node = Node(element)
        if not self.head:  
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  
            self.tail = new_node  
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        return self.size

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0: 
            self.tail = new_node
        self.size += 1
        print(f"Prepended {element} to the list")

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Print Linked list: [" + " , ".join(elements) + "]")

LinkedList = LinkedList()
LinkedList.append(8)
LinkedList.get(0)
LinkedList.set(0, 6)
LinkedList.get(0)
print(f"Current size: {LinkedList.size}")
LinkedList.prepend(10)
LinkedList.print_list()