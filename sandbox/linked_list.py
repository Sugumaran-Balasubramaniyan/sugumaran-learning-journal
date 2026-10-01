class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create Node A and Node B
node_a = Node("A")
node_b = Node("B")

# Link Node A to Node B
node_a.next = node_b

# Let's verify the chain
print(f"Node A value: {node_a.value}")
print(f"Node A's next points to: {node_a.next}")       # This is node_b's object reference
print(f"Value of Node A's next: {node_a.next.value}")  # This prints "B"
print(f"Node B's next points to: {node_b.next}")       # This is None