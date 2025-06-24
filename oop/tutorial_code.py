"""
Object Oriented Programming (OOP) Basics Tutorial
Subtopics:
- Classes and Objects
- Attributes and Methods
- Constructors (__init__)
- Inheritance
- Encapsulation
- Simple Example
"""

# Classes and Objects
class Dog:
    # Attributes and Methods
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof!")

# Creating an object
my_dog = Dog("Buddy", 3)
print("Dog's name:", my_dog.name)
print("Dog's age:", my_dog.age)
my_dog.bark()

# Inheritance
class GuideDog(Dog):
    def guide(self):
        print(f"{self.name} is guiding their owner.")

guide_dog = GuideDog("Max", 5)
guide_dog.bark()
guide_dog.guide()

# Encapsulation (using _ for protected, __ for private)
class Cat:
    def __init__(self, name):
        self._mood = "happy"  # protected
        self.__name = name    # private
    def get_name(self):
        return self.__name

cat = Cat("Whiskers")
print("Cat's name:", cat.get_name())
