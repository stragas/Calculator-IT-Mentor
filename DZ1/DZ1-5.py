person = {
    "name": "Alice",
    "age": 30,
    "gender": "Female",
    "height": 165,
    "weight": 60,
    "foot size": 25
}

for key, value in person.items():
    print(f"{key}: {value}")

person["foot size"] = 18

#person.pop("age")
del person["age"]

for key, value in person.items():
    print(f"{key}: {value}")

print(person)

