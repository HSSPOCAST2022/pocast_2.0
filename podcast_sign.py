import streamlit as st
from pandas import DataFrame
from google.oauth2 import service_account
from gspread_pandas import Spread,Client

# Create a connection object.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Create a Google Authentication connection object
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "podcast test"
spread = Spread(spreadsheetname,client = client)
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()

def load_the_spreadsheet(spreadsheetname):
    worksheet = sh.worksheet(spreadsheetname)
    df = DataFrame(worksheet.get_all_records())
    return df
def update_the_signup_spreadsheet(dataframe):
    col = ['Date','Block 1', 'Block 2', 'Block 3', 'Lunch A', 'Lunch B', 'Block 5', 'Block 6']
    spread.df_to_sheet(dataframe[col],sheet = 'Sign-up name',index = False)
def update_the_nameOfPeople_spreadsheet(dataframe):
    col = ['Date','Name of the person who regster','Email of the person who regster', 'Other 1', 'Other 2', 'Other 3']
    spread.df_to_sheet(dataframe[col],sheet = 'name of people recording',index = False)

def sign_up_from():
    st.title('Podcast Sign-up Form')
    firstLastName = st.text_input("Your First and Last Name")
    email = st.text_input("Write your school email")
    date = st.date_input('Which day do you want to record?')
    block = st.selectbox("Select a Block", ('Block 1', 'Block 2', 'Block 3', 'Lunch A', 'Lunch B', 'Block 5', 'Block 6'))
    if block == 'Block 1':
        block1 = firstLastName
    else:
        block1 = ' '
    if block == 'Block 2':
        block2 = firstLastName
    else:
        block2 = ' '
    if block == 'Block 3':
        block3 = firstLastName
    else:
        block3 = ' '
    if block == 'Lunch A':
        lunchA = firstLastName
    else:
        lunchA = ' '
    if block == 'Lunch B':
        lunchB = firstLastName
    else:
        lunchB = ' '
    if block == 'Block 5':
        block5 = firstLastName
    else:
        block5 = ' '
    if block == 'Block 6':
        block6 = firstLastName
    else:
        block6 = ' '
    st.write("List the names of the people who will be recording with you in the boxes below.  One name per box.  If you have less than 3 additional members, type N/A in the box that is blank.")
    name2_1 = st.text_input("Name of person one")
    name3_1 = st.text_input("Name of person two")
    name4_1 = st.text_input("Name of person three")
    if st.button("Submit"):
        with st.spinner('Wait for it...'):
            opt = { 'Date': [date],
            'Block 1' : [block1],
            'Block 2': [block2],
            'Block 3': [block3],
            'Lunch A': [lunchA],
            'Lunch B': [lunchB],
            'Block 5': [block5],
            'Block 6': [block6]}
            opt_df = DataFrame(opt)
            df = load_the_spreadsheet('Sign-up name')
            new_df = df.append(opt_df,ignore_index=True)
            update_the_signup_spreadsheet(new_df)
            opt2 = {'Date' :[date],
            'Name of the person who regster' : [firstLastName],
            'Email of the person who regster' : [email],
            'Other 1': [name2_1],
            'Other 2': [name3_1],
            'Other 3': [name4_1]}
            opt2_df = DataFrame(opt2)
            df2 = load_the_spreadsheet('name of people recording')
            new_df2 = df2.append(opt2_df,ignore_index=True)
            update_the_nameOfPeople_spreadsheet(new_df2)
        st.success("You are good to go.")
        st.balloons()