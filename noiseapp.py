import start_screen
import streamlit as st
import subprocess



def app():
    if start_screen.x == None:
        st.info("no image was selected")

    elif start_screen.x != None:
        
            #Todo 
            #alhough this works it will be best to change this section to be more pythonic
            #instead of runing subprocess
            status_text = st.empty()
            progress_bar = st.progress(0)
            # with st.spinner("executing noisprint"):
            status_text.text('generating noiseprint:')
            progress_bar.progress(25)
            subprocess.call("python main_blind.py {} ref.mat".format(start_screen.x), shell=True)
            progress_bar.progress(50)
            subprocess.call("python main_map2uint8.py ref.mat out-heat.png", shell=True)
            progress_bar.progress(75)
            status_text.text('computing heatmap:')
            subprocess.call("python main_showres.py {} out-heat.png ref.mat".format(start_screen.x), shell=True)
            progress_bar.progress(100)
            status_text.text('Done!')
            st.balloons()
            st.image("heatmap.png")