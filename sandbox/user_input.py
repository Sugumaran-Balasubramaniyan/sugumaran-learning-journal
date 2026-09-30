age = int(input("Enter your age:"))

if age < 13:
    print("under 13")
elif age >= 13 and age <= 17:
    print("between 13 and 17")
elif age > 17:
    print("18 or older")