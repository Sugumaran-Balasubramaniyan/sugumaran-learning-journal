with open("sandbox/learning.txt", "w") as file:
    file.write("I am learning Python")

with open("sandbox/learning.txt", "r") as file:
    content = file.read()

print(content)

with open("sandbox/learning.txt", "a") as file:
    file.write("\nMore Python practice")

with open("sandbox/learning.txt", "r") as file:
    for line in file:
        print(line.strip())