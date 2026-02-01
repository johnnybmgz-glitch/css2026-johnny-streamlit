import streamlit as st

st.set_page_config(
    page_title="Johnny – CSS 2026",
    page_icon="👨🏾‍💻",
    layout="wide"
)

# HEADER
st.title("Johnny Lukanka")
st.subheader("Coding Summer School 2026")
st.markdown("> *Whatever you do, as long as you choose to do it, dedicate your heart*")

st.write("""
This is my public Streamlit website.  
It presents my profile and my work.
""")

# ABOUT ME
st.header("About Me")
st.write("""
My name is Johnny, and I am passionate about technology and continuous learning.
I enjoy creating, testing, fixing, and starting again until it works and I understand why.

Through my projects, I am building skills in programming, data, 
and website development, with a practical and progressive approach. 
This website reflects my journey, my efforts, and my desire to turn 
learning into something concrete and personal.
""")

# WORKING ON
st.subheader("I'm currently working on")
st.markdown("""
- Learning Python fundamentals  
- Building data pipelines  
- Creating Streamlit web apps  
""")

# PASSIONS / CARS
st.header("Things I Like")

st.image("Landcruiser1.jpeg", use_container_width=True)
st.caption("My favourite one – Toyota LandCruiser")

st.image("Ford1.avif", use_container_width=True)
st.caption("My second one – Ford Ranger")

st.image("DodgeRam.jpg", use_container_width=True)
st.caption("My third one – Dodge Ram")
