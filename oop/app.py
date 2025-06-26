import streamlit as st

st.title("Object Oriented Programming (OOP) Basics Tutorial")
st.markdown("""
This interactive app demonstrates OOP concepts in Python:
- Classes and Objects
- Attributes and Methods
- Constructors (__init__)
- Inheritance
- Encapsulation
""")

# --- Classes and Objects ---
st.header("1. Classes and Objects")
with st.expander("Show Dog class code"):
    st.code('''class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    def bark(self):\n        print(f"{self.name} says woof!")''', language='python')

st.subheader("Create a Dog object")
dog_name = st.text_input("Dog's name", "Buddy")
dog_age = st.number_input("Dog's age", min_value=0, max_value=30, value=3)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says woof!"

if st.button("Create Dog and Bark!"):
    my_dog = Dog(dog_name, dog_age)
    st.success(f"Dog's name: {my_dog.name}")
    st.success(f"Dog's age: {my_dog.age}")
    st.info(my_dog.bark())

# --- Inheritance ---
st.header("2. Inheritance")
with st.expander("Show GuideDog class code"):
    st.code('''class GuideDog(Dog):\n    def guide(self):\n        print(f"{self.name} is guiding their owner.")''', language='python')

guide_name = st.text_input("Guide Dog's name", "Max")
guide_age = st.number_input("Guide Dog's age", min_value=0, max_value=30, value=5)

class GuideDog(Dog):
    def guide(self):
        return f"{self.name} is guiding their owner."

if st.button("Create GuideDog and Demonstrate!"):
    guide_dog = GuideDog(guide_name, guide_age)
    st.success(guide_dog.bark())
    st.info(guide_dog.guide())

# --- Encapsulation ---
st.header("3. Encapsulation")
with st.expander("Show Cat class code"):
    st.code('''class Cat:\n    def __init__(self, name):\n        self._mood = "happy"  # protected\n        self.__name = name    # private\n    def get_name(self):\n        return self.__name''', language='python')

cat_name = st.text_input("Cat's name", "Whiskers")

class Cat:
    def __init__(self, name):
        self._mood = "happy"  # protected
        self.__name = name    # private
    def get_name(self):
        return self.__name

if st.button("Create Cat and Show Name"):
    cat = Cat(cat_name)
    st.success(f"Cat's name: {cat.get_name()}")
    st.info("Try accessing _mood or __name directly in code to see encapsulation in action!")

st.markdown("---")
st.markdown("Created for the Oxford AI Summit OOP Tutorial. Explore the code and try different names/ages!")
