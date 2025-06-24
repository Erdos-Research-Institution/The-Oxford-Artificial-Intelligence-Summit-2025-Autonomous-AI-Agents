"""
Python Basics Tutorial
Subtopics:
- Variables and Data Types
- Input and Output
- Control Flow
- Loops
- Functions
- Lists and Basic Operations
"""

# Variables and Data Types
x = 5           # integer
name = "Alice"  # string
pi = 3.14       # float
is_valid = True # boolean

print("Variables:", x, name, pi, is_valid)

# Input and Output
user_name = input("Enter your name: ")
print("Hello,", user_name)

# Control Flow
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Functions
def greet(person):
    print(f"Hello, {person}!")

greet(user_name)

# Lists and Basic Operations
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
fruits.append("orange")
print("After adding orange:", fruits)
print("First fruit:", fruits[0])
for fruit in fruits:
    print("I like", fruit)
