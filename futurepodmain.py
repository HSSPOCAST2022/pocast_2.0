import streamlit as st
from streamlit_option_menu import option_menu
from dont_mess import home,config,hide_st
from podcast_sign import sign_up_from
from pod_instructions import instructions
from Admin import admin
from audio_podcast import audio
from video_podcast import video

config()
hide_st()

def main():
    st.cache()
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Sutudents in WW-P HSS', 'Podcast sign-up form','Audio podcast','Video podcast','Admin'],
            icons=['house-door-fill','list', 'card-checklist','mic-fill','file-play-fill','person-fill'],
            menu_icon='cast'
    )
    if selected == 'Home':
        home()
    if selected == 'Sutudents in WW-P HSS':
        instructions()
    if selected == 'Podcast sign-up form':
        sign_up_from()
    if selected == 'Audio podcast':
        audio()
    if selected == 'Video podcast':
        video()
    if selected == 'Admin':
        admin()
if __name__ == "__main__":
  main()

