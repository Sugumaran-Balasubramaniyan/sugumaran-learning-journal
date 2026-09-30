person = {
    "name": "Sugumaran",
    "age": 20,
    "fav_language": "Python"
}

print(person["name"])

person["goal"] = "Become the best"

person["fav_language"] = "Java"

for key, value in person.items():
    print(key, value)

