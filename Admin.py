import streamlit as st

def podcast_audio(file_name : str,date:str,name_of_the_auther:str,type_of_podcast:str,tittle_of_podcast:str,Description_of_the_Podcast:str):
    st.header(date)
    st.subheader(tittle_of_podcast)
    st.caption(f'By: {name_of_the_auther}')
    st.write(f'Type of Podcast: {type_of_podcast}')
    st.write(Description_of_the_Podcast)
    st.audio(f'Podcast/{file_name}', format= 'audio/mp3')

def podcast_video(file_name:str,date:str,name_of_the_auther:str,type_of_podcast:str,tittle_of_podcast:str,Description_of_the_Podcast:str):
    st.header(date)
    st.subheader(tittle_of_podcast)
    st.caption(f'By: {name_of_the_auther}')
    st.write(f'Type of Podcast: {type_of_podcast}')
    st.write(Description_of_the_Podcast)
    st.video(f'Podcast/{file_name}', format= 'video/mp4')



def admin():
    st.header('Admin login')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password',type='password')
    if st.sidebar.checkbox("Login"):
        if password == 'ADMINOFHSS':
            st.success(f'Logined as {username}')
            tab1, tab2 = st.tabs(['Audio Podcast Uplode','Video Podcast Uploade'])
            with tab1:
                st.subheader('Audio Podcast Uplode')

            with tab2:
                st.subheader('Video Podcast Uploade')

        else:
            st.warning('Your not the Admin')



