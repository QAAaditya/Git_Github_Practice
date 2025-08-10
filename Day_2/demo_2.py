"""
Python Data Structures Playground
---------------------------------
A file containing examples of basic Python data structures:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
You can modify, extend, or break parts of this code to practice Git concepts.
"""

# ===== Strings =====
my_string = "Hello, Git World!"
print("Original String:", my_string)
print("Uppercase:", my_string.upper())
print("Replaced:", my_string.replace("Git", "Python"))
print("Slice [0:5]:", my_string[0:5])
print("Reversed:", my_string[::-1])
print()

# ===== Lists =====
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)
fruits.append("date")
fruits.insert(1, "blueberry")
print("After Insertions:", fruits)
fruits.remove("banana")
print("After Removal:", fruits)
print("Sorted List:", sorted(fruits))
print()

# ===== Tuples =====
coordinates = (10.5, 20.3)
print("Tuple:", coordinates)
print("First Element:", coordinates[0])
# coordinates[0] = 5  # Uncomment to see tuple immutability error
print()

# ===== Sets =====
unique_numbers = {1, 2, 3, 2, 1}
print("Original Set:", unique_numbers)
unique_numbers.add(4)
unique_numbers.update([5, 6])
print("Updated Set:", unique_numbers)
unique_numbers.discard(2)
print("After Discard:", unique_numbers)
print("Set Union:", unique_numbers.union({10, 11}))
print("Set Intersection:", unique_numbers.intersection({3, 4, 5}))
print()

# ===== Dictionaries =====
person = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}
print("Original Dictionary:", person)
person["email"] = "alice@example.com"
print("After Adding Email:", person)
person["age"] = 26
print("After Updating Age:", person)
del person["city"]
print("After Deleting City:", person)

print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# ===== Mini Challenge =====
# Change this list into a dictionary of fruit lengths
