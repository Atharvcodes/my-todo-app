import streamlit as st
import funtions

todos=funtions.get_todos()

def add_todo():
    todo=st.session_state['new_todo']+'\n'
    todos.append(todo)
    funtions.write_todos(todos)

st.title("My to-do app")
st.subheader("This is my to do app.")
st.write("This app will inncrease yor productivity.")
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        funtions.write_todos(todos)
        st.rerun()

st.text_input(label=" ",placeholder="Add new todo...",
              on_change=add_todo,key='new_todo')

