class Node:
    def __init__(self, value):
        self.value = value
        self.next = None




# Create Nodes
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")

# Head node
head_node = node_a

# tail node
tail_node = node_e

# Link Nodes
node_d.next = head_node
node_a.next = node_b
node_b.next = node_c




# update head node
head_node = node_d

current_node = head_node

# Adding new node in the tail
while current_node is not None:
    if current_node.next == None:
        last_node = current_node
    current_node = current_node.next

last_node.next = tail_node

# Let's verify the chain
start_node = head_node
while start_node is not None:
    print(start_node.value)
    start_node = start_node.next