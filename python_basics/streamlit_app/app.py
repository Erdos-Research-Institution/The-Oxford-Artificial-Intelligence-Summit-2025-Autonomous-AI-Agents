import streamlit as st

st.title("Python Basics Tutorial")
st.markdown("""
### Subtopics
- Variables and Data Types
- Input and Output
- Control Flow
- Loops
- Functions
- Lists and Basic Operations
""")

st.header("Variables and Data Types")
x = 5
name = "Alice"
pi = 3.14
is_valid = True
st.write(f"x = {x} (int)")
st.write(f"name = {name} (str)")
st.write(f"pi = {pi} (float)")
st.write(f"is_valid = {is_valid} (bool)")

st.header("Input and Output")
user_name = st.text_input("Enter your name:", "Alice")
if user_name:
    st.write(f"Hello, {user_name}")

st.header("Control Flow")
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=18)
if age >= 18:
    st.write("You are an adult.")
else:
    st.write("You are a minor.")

st.header("Loops")
st.write("Counting from 1 to 5:")
for i in range(1, 6):
    st.write(i)

st.header("Functions")
def greet(person):
    return f"Hello, {person}!"
if user_name:
    st.write(greet(user_name))

st.header("Lists and Basic Operations")
fruits = ["apple", "banana", "cherry"]
if st.button("Add orange to fruits"):
    fruits.append("orange")
st.write("Fruits:", fruits)
st.write(f"First fruit: {fruits[0]}")
for fruit in fruits:
    st.write(f"I like {fruit}")
