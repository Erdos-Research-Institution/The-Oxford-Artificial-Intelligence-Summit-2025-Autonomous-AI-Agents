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
loop_num = st.slider("Select a number for loop demonstration:", min_value=2, max_value=6, value=5)
st.write(f"Counting from 1 to {loop_num}:")
for i in range(1, loop_num + 1):
    st.write(i)

st.header("Functions")
def greet(person):
    return f"Hello, {person}!"
if user_name:
    st.write(greet(user_name))

st.header("Lists and Basic Operations")
if "fruits" not in st.session_state:
    st.session_state.fruits = ["apple", "banana", "cherry"]
add_fruit = st.text_input("Add a fruit:")
if st.button("Add fruit") and add_fruit:
    if add_fruit not in st.session_state.fruits:
        st.session_state.fruits.append(add_fruit)
remove_fruit = st.selectbox("Remove a fruit:", options=["None"] + st.session_state.fruits)
if st.button("Remove selected fruit") and remove_fruit != "None":
    st.session_state.fruits.remove(remove_fruit)
st.write("Fruits:", st.session_state.fruits)
if st.session_state.fruits:
    st.write(f"First fruit: {st.session_state.fruits[0]}")
    for fruit in st.session_state.fruits:
        st.write(f"I like {fruit}")
