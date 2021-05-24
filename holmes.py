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


st.sidebar.title('Navigation')


# openm = st.button("Open image")
# if openm:
#     start_screen.x = start_screen.load_file()

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
col1,col2 = st.beta_columns((1,2))
try:
    img = Image.open(start_screen.x)
    with col1:
        st.image(img)        
except (NameError,AttributeError,FileNotFoundError):
    st.info("Images must be in ('jpg','png', or '.bmp') formats")


    
##? radio buttons logic
tools = st.sidebar.selectbox('Analysis',
    ["Summary","Metadata", "Quantization","ELA","Noiseprint"])

if tools == "Summary" and start_screen.x != None:
    import exifview
    p = exifview.exif_meta(str(start_screen.x))
    with col2:
        st.write("Path: {}".format(start_screen.x))
        if "Windows Photo Editor" in p.get("Software"):
            st.error("Editing software detected")
        else:
            st.success("No specifed editing software found")

if tools == "Metadata":
    metadata.app()
    
elif tools == "ELA":
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