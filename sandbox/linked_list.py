class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create Node A and Node B
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

# Link Node A to Node B
node_a.next = node_b
node_b.next = node_c

# Let's verify the chain
current = node_a

while current is not None:
    print(current.value)
    current = current.next

