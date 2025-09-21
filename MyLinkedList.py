class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __iter__(self):
        current = self.head

        while current != None:
            yield current.data
            current = current.next

    def __len__(self):
        return self._size
    
    def __str__(self):
        current = self.head
        f = ''

        while current != None:

            f = f  + f'{current.data}'

            if current.next != None:
                f = f + ' -- '

            current = current.next
        
        if self._size == 0:
            return "No trains :("
        
        return f
    
    def is_empty(self):
        if len(self) == 0: return True
        return False

    def append(self, data):
        new_node = self.Node(data)

        if self._size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, data):
        new_node = self.Node(data)

        if self._size == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1

    def get(self, index):
        current = self.head
        i = 0

        if index < 0 or index >= len(self): raise IndexError
        
        while i < index:

            current = current.next
            i += 1

        return current.data

    def insert_at(self, index, data):
        new_node = self.Node(data)
        current = self.head
        i = 0

        if index > len(self) or index < 0: raise IndexError

        if index == 0:

            if len(self) == 0:
                self.head = new_node
                self.tail = new_node
                self._size += 1
                return

            new_node.next = current
            self.head = new_node
            self._size += 1
            return

        if index == len(self):
            self.append(data)
            return

        while i + 1 != index:
            i += 1
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, index):
        current = self.head
        i = 0

        if index < 0 or index >= len(self): raise IndexError

        if index == 0:

            if self.head.next == None:
                self.head = None
                self.tail = None
                self._size -= 1
                return
            
            self.head = self.head.next
            self._size -= 1
            return
        
        while i + 1 != index:
            i += 1
            current = current.next

        to_remove = current.next
        current.next = to_remove.next
        self._size -= 1
        
        if to_remove.next is None:
            self.tail = current
    
    def find_index(self, data):
        current = self.head
        i = 0

        while current != None:
            if current.data == data:
                return i
            i += 1
            current = current.next
    
        return None
    
    def to_list(self):
        current = self.head
        train = []

        while current != None:
            train.append(current.data)

            current = current.next

        return train
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

            

