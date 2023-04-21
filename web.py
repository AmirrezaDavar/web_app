import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_user_on_web = st.session_state["new_todo_input"] + "\n"
    todos.append(todo_user_on_web)
    functions.write_todos(todos)


st.title("MY todo app")
st.subheader("This is my todo app in web")
st.write("This app is to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        # write the updated todos with the to-do being removed
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo_input")

