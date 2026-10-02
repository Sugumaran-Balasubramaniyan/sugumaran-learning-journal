class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
     def __init__(self):
        self.head = None
     def append(self, value):
        cursor = self.head
        if cursor is None:
            self.head = Node(value)
        else:
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = Node(value)
     def display(self):
         cursor = self.head
         while cursor is not None:
             print(cursor.value)
             cursor = cursor.next
     def contains(self, target):
         cursor = self.head
         while cursor is not None:
             if cursor.value == target:
                 return True
             else:
                 cursor = cursor.next
         if cursor is None:
             return False
         

a = LinkedList()

a.append("A")

print(a.head.value)

a.append("B")

a.display()
   


