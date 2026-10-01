def introduce(name, role="learner"):
    return "Hello " + name + " you are a " + role

print(introduce("Sugumaran"))

print(introduce("Sugumaran", "student"))

print(introduce(name="Sugumaran", role="Teacher"))

