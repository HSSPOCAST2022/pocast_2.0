import streamlit as st
from Admin import podcast_audio

def audio():
    st.title('Audio Podcast')
    podcast_audio('test1.mp3','12/22/22','AC','sound','Test1','test for podcast')