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
                 print("Match")
                 return True
             else:
                 cursor = cursor.next
         if cursor is None:
             print("No Match")
             return False
     def remove(self, target):
         cursor = self.head
         previous = None
         while cursor is not None:
             if cursor.value != target:
                 previous = cursor
                 cursor = cursor.next
             elif cursor.value == target:
                 if previous is None:
                     self.head = cursor.next
                     return True
                 previous.next = cursor.next
                 return True
         return False

             
             
             

a = LinkedList()

a.append("A")
a.append("B")
a.append("C")

print("Full list:")
a.display()

a.contains("B")

a.remove("B")

print("List after removing B:")
a.display()

a.remove("A")

print("List after removing A:")
a.display()


   


