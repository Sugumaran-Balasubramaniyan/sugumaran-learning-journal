class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
     def __init__(self):
         self.root = None
     
     def insert(self, value):
         current = self.root
         if current is None:
             self.root = Node(value)
             return

         while True:
             if value < current.value:
                 if current.left is None:
                     current.left = Node(value)
                     return
                 current = current.left
             elif value > current.value:
                 if current.right is None:
                     current.right = Node(value)
                     return
                 current = current.right
             else:
                 return

     def contains(self, target):
         current = self.root
         while current is not None:
             if target == current.value:
                 return True
             elif target < current.value:
                 current = current.left
             else:
                 current = current.right
         return False

     def in_order(self):
         values = []

         def visit(node):
             if node is None:
                 return
             visit(node.left)
             values.append(node.value)
             visit(node.right)

         visit(self.root)
         return values


         




root = Node(4)
root.left = Node(2)
root.right = Node(6)

print(root.left.value, root.value, root.right.value)  # 2 4 6


tree = BinarySearchTree()
for value in (8, 3, 10, 6):
    tree.insert(value)

print(tree.root.left.right.value)  # 6

print(tree.in_order())
