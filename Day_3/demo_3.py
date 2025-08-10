"""
Data Structures Interactive Examples
-------------------------------------
This script demonstrates Python's built-in data structures:
- String
- List
- Tuple
- Set
- Dictionary
Includes user input and small challenges for Git experimentation.
"""

# ===== Strings =====
name = "John Doe"
greeting = f"Hello, {name}!"
print("Greeting:", greeting)
print("Length of name:", len(name))
print("First 4 letters:", name[:4])
print("Replace Doe -> Smith:", name.replace("Doe", "Smith"))
print()

# ===== Lists =====
numbers = [10, 20, 30, 40, 50]
print("Numbers List:", numbers)
numbers.append(60)
numbers.extend([70, 80])
print("After Adding:", numbers)
numbers.pop(2)  # remove element at index 2
print("After Removing Index 2:", numbers)
print("Sum of Numbers:", sum(numbers))
print()

# ===== Tuples =====
colors = ("red", "green", "blue")
print("Tuple of Colors:", colors)
print("Index of 'green':", colors.index("green"))
print("Count of 'red':", colors.count("red"))
print()

# ===== Sets =====
animals = {"cat", "dog", "bird"}
print("Animals Set:", animals)
animals.add("fish")
animals.update(["lion", "tiger"])
print("After Add/Update:", animals)
animals.discard("cat")
print("After Discard:", animals)
print("Is 'dog' in animals?:", "dog" in animals)
print()

# ===== Dictionaries =====
student = {
    "name": "Emma",
    "age": 22,
    "major": "Computer Science"
}
print("Student Dictionary:", student)
student["graduated"] = False
student["age"] += 1
print("After Updates:", student)

# Iterating through dictionary
print("Keys and Values:")
for key, value in student.items():
    print(f"{key}: {value}")

# ===== Small Practice Task =====
# Convert a list of words into a dictionary mapping word -> length
words = ["python", "git", "branch", "merge"]
word_lengths = {word: len(word) for word in words}
print("\nWord Lengths Dictionary:", word_lengths)

def from_branch_3():
    pass