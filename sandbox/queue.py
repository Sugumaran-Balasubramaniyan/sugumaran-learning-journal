class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        # add items to the list or queue
        self.items.append(value)

    def display(self):
        print(self.items)

    def dequeue(self):
        try:
            first = self.items.pop(0)
            return first
        except IndexError:
            return None

queue = Queue()

# Adding A to the queue
print("Adding A to the queue:")
queue.enqueue("A")

# Dispplaying the queue
print("Displaying the queue:")
queue.display()

# Adding B to the queue
print("Adding B to the queue:")
queue.enqueue("B")

# Displaying the queue
print("Displaying the queue:")
queue.display()

# Adding C to the queue
print("Adding C to the queue:")
queue.enqueue("C")

# Removing the first item from the queue
popped_value = queue.dequeue()

# Displaying the removed value from the queue
print("The first item removed from the queue:")
print(popped_value)

# Removing the second item from the queue
popped_value = queue.dequeue()

# Displaying the removed value from the queue
print("The second removed item from the queue:")
print(popped_value)

# Removing the third item from the queue
popped_value = queue.dequeue()

# Displaying the removed value from the queue
print("The third removed item from the queue:")
print(popped_value)

# Displaying the queue
print("The final queue is:")
queue.display()

empty_queue = queue.dequeue()
print("Empty queue:", empty_queue)