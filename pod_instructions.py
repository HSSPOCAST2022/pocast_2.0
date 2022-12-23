import streamlit as st

write = """
Recordings without a chromebook:-
    \n\t1.Find the power cord at bottom of the cart and plug it to the wall
    \n\t2.Take a note of the number on your headset this corresponds to a channel on the control board
    \n\t3.Important! Adjust your voice levels to create a balanced sound (make sure the Green Dot are within the green lines)
    \n\t4.Press mute for unused microphones
    \n\t5.Press the “Record” button to begin recording
    \n\t6.When finished,  press “Record” again

Transferring your recording from the control panel to laptop or to a Chromebook:-
    \n\t1.Login to the media center podcasting Dell laptop (use your first part of your email address and password) or  you can use your Chromebook to transfer the recording 
    \n\t2.Connect the USB cord from the control panel to the  Dell laptop  or your Chromebook
    \n\t3.Click on micro SD icon on the control panel Which is next to the music symbol icon
    \n\t4.Click on podcast transfer mode
    \n\t5.Click yes to transfer the recording
    \n\t6.If you're using your Chromebook 
        \n\t\ta.Then go to the files app on your Chromebook
        \n\t\tb.Then you should see RODECASTER At the bottom left in the file app
        \n\t\tc.Double click on RODE
        \n\t\td.Double click on podcasts
        \n\t\te.Double click (or select) audio recordings you recorded
    \n\t7.If you're using the Dell laptop
        \n\t\ta.then go to file explorer on the laptop 
        \n\t\tb.Then click on this PC
        \n\t\tc.Then you should see RODECASTER and  double click on it
        \n\t\td.Double click on RODE
        \n\t\te.Double click on podcasts
        \n\t\tf.End the first audio recording is you're recording
    \n\t8.Rename the podcast
    \n\t9.choose the platform anchor for your MP3 file
    \n\t10.save the MP3 file to downloads
    \n\t11.email the file to  yourself and added to drive
    \n\t12.Click “done” on the control panel

Removing your podcast from the control panel:-
    \n\t1.Click on the settings icon
    \n\t2.Press  podcast
    \n\t3.press the trash icon

Connecting Bluetooth devices to the control panel:-
    \n\t1.Turn on Bluetooth on the device that you choose to connect to the control panel
    \n\t2.Click on the Bluetooth symbol on the control panel 
    \n\t3.Now on your Bluetooth device  you should search for a name of a device  called “RODECASTER PRO”
    \n\t4.Click on that device name  and you should be connected to the control panel.

Adjusting the volume of the Bluetooth devices:-
    \n\t1.Under the Bluetooth button you should see a slider
    \n\t2.You can move the slider up and down to adjust the volume of the background  music.

"""
def instructions():
    st.title('Sutudents in WW-P HSS')
    st.header('Writen instructions for podcast station')
    st.markdown(write)