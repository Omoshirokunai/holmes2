"""
metadata viewer

This script extracts the exif metadata from the image in main.py and displays it in a streamlit dataframe
"""
import streamlit as st  
from skimage.io import imread
import pandas as pd
import exifview
import start_screen



def app():
    st.header("Metadata")
    st.info("Metadata is infornamtion embeded within an image that informs about the settings used to capture a scene as well as infornmation about the camera and editing software used")
    try:
        im = str(start_screen.x)
        
        p = exifview.exif_meta(im)
        if p:
            df = pd.DataFrame(list(p.items()),columns = ['exif','values'])
            st.dataframe(df,900,500)
        else:
            st.error("Sorry No Exif Found :crying_cat_face:")
    except (AttributeError,FileNotFoundError):
        st.error("no image selected")
        
        
    
        