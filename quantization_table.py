"""
Quantiztion table viewer

this is a script that extracts chrominance and luminace quantization tables of an image
then from a list of available tables we can deduce the software used to export the image this can come in handy in cases where
metadata has also been tampered with or is not available.
"""
import streamlit as st
import jpegio as jio 
import start_screen
import numpy as np
def app():
    try:
        #get file object
        
        jpeg = jio.read(start_screen.x)  
        col1, col2 = st.beta_columns(2)
        # coef_array = jpeg.coef_arrays[0]  
        with col1:
            qtlum = jpeg.quant_tables[0]
            qtlum = np.array(qtlum)
            st.write("luminance",qtlum)
            
        with col2:
            qtchrom = jpeg.quant_tables[1]
            qtchrom = np.array(qtchrom)
            st.write("Chrominace",qtchrom)
        
        #find qtable matches
        st.write("Matches")
        file1 = open("quantable_class\\sample.txt", "r+")
        line = file1.readlines()
        lumline = line[2:9]
        file1.close
        lumin = np.array([x[:-1] for x in lumline])

        comparison = lumin == qtlum.astype(str)
        print(lumin)
        equal_arrays = comparison.all()
        print(equal_arrays)
        
    except AttributeError:
        st.error("no image selected")
    

    