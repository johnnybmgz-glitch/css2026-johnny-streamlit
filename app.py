# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 18:44:34 2026

@author: User
"""
import streamlit as st

st.set_page_config(layout="wide")

st.set_page_config(
    page_title="Johnny – CSS 2026",
    page_icon="👨🏾‍💻"
)

st.title("Johnny Lukanka")
st.subheader("Coding Summer School 2026")
st.subheader("Whatever you do, as long as you choose to do it, dedicate your heart")
st.write("""
This is my public Streamlit website.
It presents my profile and my work.
""")

st.header("About Me")
st.write("""
My name is Johnny, and I am passionate about technology and continuous learning.
I enjoy creating, testing, fixing, and starting again until it works and I understand why.

Through my projects, I am building skills in programming, data, 
and website development, with a practical and progressive approach. 
This website reflects my journey, my efforts, and my desire to turn 
learning into something concrete and personal.
""")
st.subheader("I'm working on")
st.markdown("""
- Learning Python fundamentals  
- Building data pipelines  
- Creating Streamlit web apps
""")
st.image("Landcruiser1.jpeg", width=2200)
st.markdown("""
This is not the best car in the world, but it's my favourite, the first one! Toyota LandCruiser
""")

st.image("Ford1.avif", width=2200)
st.markdown("""
This is my second one, a Ford Ranger
""")

st.image("DodgeRam.jpg", width=2200)
st.markdown("""
This is my third one, a DodgeRam
""")






