import streamlit as st

st.set_page_config(
    page_title="Mpr Demo",
    page_icon=">>"
)

st.title("MULTIMODAL GENERATIVE AI FOR WEBPAGE CREATION WITH TEXT AND IMAGE")
st.header("Group No : 6")
st.page_link("Homepage.py", label="HomePage", icon="🏠")
st.page_link("pages/1_Text to Text Model.py", label="Text Model", icon="1️⃣")
st.page_link("pages/2_Image to Text Model.py", label="Image to Text Model", icon="2️⃣")
