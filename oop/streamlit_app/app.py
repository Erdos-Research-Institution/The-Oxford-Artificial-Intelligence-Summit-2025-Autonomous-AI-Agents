import streamlit as st

st.title("Object Oriented Programming (OOP) Basics Tutorial")
st.markdown("""
### Subtopics
- Classes and Objects
- Attributes and Methods
- Constructors (__init__)
- Inheritance
- Encapsulation
- Simple Example
""")

st.header("Classes and Objects")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)
st.write(f"Dog's name: {my_dog.name}")
st.write(f"Dog's age: {my_dog.age}")
st.write(my_dog.bark())

st.header("Inheritance")
class GuideDog(Dog):
    def guide(self):
        return f"{self.name} is guiding their owner."

guide_dog = GuideDog("Max", 5)
st.write(guide_dog.bark())
st.write(guide_dog.guide())

st.header("Encapsulation")
class Cat:
    def __init__(self, name):
        self._mood = "happy"
        self.__name = name
    def get_name(self):
        return self.__name

cat = Cat("Whiskers")
st.write(f"Cat's name: {cat.get_name()}")
