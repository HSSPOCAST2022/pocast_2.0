import streamlit as st
from PIL import Image

image1 = Image.open('icon/WW-P HSS.png')
image2 = Image.open('icon/WW-P HSS copy.png')
def hide_st():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def config():
    st.set_page_config(
    page_title='HSS - Podcast ',
    page_icon= image1)

def home():
    st.title('WW-P HSS Podcast')
    col1, col2 = st.columns(2)
    with col1:
            st.image(image2)
    with col2:
            st.header('Summary')
            st.write("""WW-P HSS podcast is a compliation of HSS students history so that they can acceces there High school memory. And it as all podcast that are made by HSS students from the most funnest to most personal stories or coversation.""")
