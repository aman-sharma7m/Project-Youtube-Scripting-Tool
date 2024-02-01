import streamlit as st
from dotenv import load_dotenv
import os 
from utils import generate_script

#loading the keys 
# load_dotenv()

st.set_page_config(page_title='Youtube Script-tool',page_icon='😍')

if 'api_key' not in st.session_state:
  st.session_state['api_key']=''



#sidebar
st.sidebar.header('😎😎😎')
key=st.sidebar.text_input('enter your api key to proceed.',type='password')
submit=st.sidebar.button('Submit')
if submit:
  st.session_state['api_key']=key

#main page
st.header('Youtube Scripting Tool')
topic_query=st.text_input('Please provide the topic of the video.')
video_len=st.text_input('Estimated video length (Min)')
creativity=st.slider('Creativity:',min_value=0.0,max_value=1.0)
generate=st.button('Generate')

if generate:
    if st.session_state['api_key']!='':
       st.success('Hope you like the script!')
       script,title,search_result=generate_script(st.session_state['api_key'],topic_query,video_len,creativity)
       st.subheader('Title')
       st.write(title)
       st.subheader('your Script: ')
       st.write(script)
       st.subheader('Check duck duck go:')
       with st.expander('Show me'):
          st.info('Search data')
          st.write(search_result)

    else:
      st.error('Please provide the valid api key')
