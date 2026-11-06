

# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from PIL import Image




import streamlit as st
from app import get_gemini_response as textmodel
from pages.vision import get_gemini_response as textoimagemodel

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(page_title="Q&A Demo")
st.header("MULTIMODAL GENERATIVE AI FOR WEBPAGE CREATION WITH TEXT AND IMAGE")

modeltext = st.button("Text-to-Text Model")
modelImage = st.button("Text-to-Image Model")


def text_to_text_model():
    st.header("Text-to-Text Model")

    input=st.text_input("Input: ",key="input")


    submit=st.button("Ask the question")

    ## If ask button is clicked

    st.write(input)
    if submit:
        response=textmodel(input)
        st.subheader("The Response is")
        st.write(response)

def image_to_text_model():
    st.header("Image-to-Text Model")
    input=st.text_input("Input Prompt: ",key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Tell me about the image")

    ## If ask button is clicked

    if submit:
        
        response=textoimagemodel(input,image)
        st.subheader("The Response is")
        st.write(response)
        


if modeltext:
    # text_to_text_model()
    st.header("Text-to-Text Model")

    input=st.text_input("Input: ",key="input")


    submit=st.button("Ask the question")

    ## If ask button is clicked

    st.write(input)
    if submit:
        response=textmodel(input)
        st.subheader("The Response is")
        st.write(response)
    

    
if modelImage:
    image_to_text_model()
   
    
   
   























































































