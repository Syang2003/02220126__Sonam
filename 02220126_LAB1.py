class CustomList:
    def __init__(self, capacity =10): #constructor of the class
        self._elements = [None] * capacity  #creating a private list (array) to store elements
        self._capacity = capacity 
        self._size = 0 #current number of elements in list
        print(f"New CustomList with capacity: {self._capacity}")
        print(f"Current size :{self._size}")
Task1 = CustomList()
    
   








