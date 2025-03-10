class CustomList:
    def __init__(self, capacity =10): #constructor of the class
        self._array = [None] * capacity  #creating a private list (array) to store elements
        self._capacity = capacity 
        self._size = 0 #current number of elements in list
        print(f"New CustomList with capacity: {self._capacity}")
        print(f"Current size :{self._size}")

    def append(self, element): #Add an element to the end of the list.
        if self._size < self._capacity:
            self._array[self._size] = element  # Insert element at the next available position
            self._size += 1  # Increase size count
            print(f"Appended {element} to the list")
        else:
            print("Error: List is at full capacity")

    def get(self, index):  #Retrieve an element at a specific index.
        if 0 <= index < self._size:
            print(f"Element at index {index}: {self._array[index]}")
            return self._array[index]
        else:
            print("Error: Index out of bounds")
            return None

    def set(self, index, element): #Replace an element at a specific index.
        if 0 <= index < self._size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Error: Index out of bounds")

    def size(self): #Return the current number of elements
        print(f"Current size: {self._size}")
        return self._size

custom_list = CustomList()

custom_list.append(8)

custom_list.get(0)

custom_list.set(0, 10)

custom_list.get(0)

custom_list.size()



