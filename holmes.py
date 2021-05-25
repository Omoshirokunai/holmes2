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
btcol1, btcol2 = st.sidebar.beta_columns(2)
with btcol1:
    openf = st.sidebar.button("Open image")
with btcol2:
    relo = st.sidebar.button("reload the app",help="reload the app")

# if stop:
#     raise StopException(None)
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
            start_screen.x = str(start_screen.get_path())
    
##? radio buttons logic
tools = st.sidebar.selectbox('Analysis',
    ["Summary","Metadata", "Quantization","ELA","Noiseprint"])



    
def summary():
    col1,col2 = st.beta_columns((1,2))
    try:
        img = Image.open(start_screen.x)
        with col1:
            st.image(img)
        with col2:
            import exifview
            p = exifview.exif_meta(str(start_screen.x))
            st.write("Path: {}".format(start_screen.x))
            if str(p.get("Software")) in ["Windows Photo Editor", "Adobe Photoshop CC 2019 (Windows)","Adobe Photoshop CC 2015.5 (Macintosh)"]:
                st.error("Editing software detected")
            else:
                st.success("No specifed editing software found")        
    except (NameError,AttributeError,FileNotFoundError):
        st.info("Images must be in ('jpg','png', or '.bmp') formats")

# with col2:
if tools == "Summary":
    st.title("Holmes image forensics toolkit")
    # if start_screen.x != None:
    summary()
else:
    try:
        img = Image.open(start_screen.x)
        st.sidebar.image(img)
    except (AttributeError,FileNotFoundError):
        pass


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
    


# stop = st.sidebar.button("Stop the app",help="force stop the app")
from streamlit.script_runner import StopException, RerunException
if relo:
    raise RerunException(None)