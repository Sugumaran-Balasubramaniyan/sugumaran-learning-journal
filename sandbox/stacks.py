class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def display(self):
        print(self.items)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None
            


stacks = Stack()

stacks.push("X")


stacks.display()

stacks.push("Y")


stacks.display()

popped_value = stacks.pop()

print(popped_value)

stacks.display()