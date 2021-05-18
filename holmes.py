"""
holmes main script

objective 1)   detect image fogery (deep learning method and other methods)

objective 2)  image analysis


This the main streamlit script that contains page navigation and image to be processed
"""
import start_screen 
import metadata
import noiseapp
import quantization_table
import streamlit as st
import ela

# import pandas as pd
from PIL import Image
import os
import subprocess

##? streamlit change options
# st.set_page_config(page_title='HOLMES', layout = "wide", initial_sidebar_state = 'auto')
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
##----##

##? gui options and titles
st.title("Welcome to Holmes :smiley_cat:")
st.sidebar.title('Navigation')

openf = st.sidebar.button("Open an image")
# opt = st.sidebar.checkbox("EXIF data",False)
# opt_ela = st.sidebar.checkbox("Error level Analysis",False,key=3)
# opt_noiseprint =  st.sidebar.checkbox("Noiseprint", value=False)
# opt_qunatization = st.sidebar.checkbox("quantization tables",False)

##--##

if openf:
    start_screen.x = None
    if start_screen.x == None:
        start_screen.x = start_screen.load_file()
        if os.path.isfile('ref.mat'):
            subprocess.call("del ref.mat && del out-heat.png && del heatmap.png", shell=True)
            # start_screen.x = str(start_screen.get_path())
try:
    img = Image.open(start_screen.x)
    col1,col2 = st.beta_columns((1,2))
    with col1:
        st.image(img)
    with col2:
        st.write("Path: {}".format(start_screen.x))
        
except (NameError,AttributeError,FileNotFoundError):
    st.info("Images must be in ('jpg','png', or '.bmp') formats")

##? radio buttons logic
tools = st.sidebar.selectbox('Advanced analysis',
    ["Summary","Metadata", "Quantization","ELA","Noiseprint"])

if tools == "Metadata":
    metadata.app()
    
elif tools == "ELA":
    st.subheader("Error level Analysis")
    ela.app()

if tools == "Quantization":
    quantization_table.app()

if tools == "Noiseprint":
    noiseapp.app()

##--##
    print("done")

relo = st.sidebar.button("reload the app",help="reload the app")
stop = st.sidebar.button("Stop the app",help="force stop the app")
from streamlit.script_runner import StopException, RerunException
if relo:
    raise RerunException(None)

if stop:
    raise StopException(None)