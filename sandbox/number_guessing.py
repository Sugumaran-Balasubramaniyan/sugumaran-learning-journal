import random

secret_number = random.randint(1, 10)

user_input = 0
while user_input != secret_number: 
    try:
        user_input = int(input("Guess the number: "))
    except ValueError:
        print("Invalid number")
        continue
    if user_input > secret_number:
        print("Too high")
    elif user_input < secret_number:
        print("Too low")
    else:
        print("Correct")

    



        