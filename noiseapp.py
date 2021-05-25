import start_screen
import streamlit as st
import subprocess



def app():
    st.header("Noiseprint")
    st.info("Noiseprint is a CNN-based camera model fingerprint extracted by a fully Convolutional Neural Network created by the Image Processing Research Group of the University Federico II of Naples, The Heatmap generated tries to estimate for each pixel, the likelihood that it has has been manipulated")
    if start_screen.x == None:
        st.error("no image selected")
    elif start_screen.x != None:
        
            #Todo 
            #alhough this works it will be best to change this section to be more pythonic
            #instead of runing subprocess
            status_text = st.empty()
            progress_bar = st.progress(0)
            # with st.spinner("executing noisprint"):
            status_text.text('generating noiseprint:')
            progress_bar.progress(25)
            subprocess.call("python main_blind.py {} ref.mat".format(start_screen.x), shell=False)
            progress_bar.progress(50)
            subprocess.call("python main_map2uint8.py ref.mat out-heat.png", shell=False)
            progress_bar.progress(75)
            status_text.text('computing heatmap:')
            subprocess.call("python main_showres.py {} out-heat.png ref.mat".format(start_screen.x), shell=True)
            progress_bar.progress(100)
            status_text.text('Done!')
            st.balloons()
            try:
                st.image("heatmap.png")
            except FileNotFoundError:
                st.error("noiseprint may not be working properly check if requirements have been properly installed")