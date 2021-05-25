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
        if start_screen.x != None:
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
            st.write("Matches found?")
            file1 = open("quantable_class\\sample.txt", "r+")
            line = file1.readlines()
            lumline = line[2:9]
            file1.close
            
            
            photoshoplum = np.array([

[[27, 26, 41, 65, 66, 39, 34, 17],
[26, 29, 38, 47, 28, 23, 12, 12],
[41, 38, 47, 28, 23, 12, 12, 12],
[65, 47, 28, 23, 12, 12, 12, 12],
[66, 28, 23, 12, 12, 12, 12, 12],
[39, 23, 12, 12, 12, 12, 12, 12],
[34, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12]],

[[20, 17, 26, 41, 51, 39, 34, 17],
[17, 18, 24, 39, 28, 23, 12, 12],
[26, 24, 32, 28, 23, 12, 12, 12],
[41, 39, 28, 23, 12, 12, 12, 12],
[51, 28, 23, 12, 12, 12, 12, 12],
[39, 23, 12, 12, 12, 12, 12, 12],
[34, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12]],

[[20, 16, 25, 39, 50, 46, 62, 68],
[16, 18, 23, 38, 38, 53, 65, 68],
[25, 23, 31, 38, 53, 65, 68, 68],
[39, 38, 38, 53, 65, 68, 68, 68],
[50, 38, 53, 65, 68, 68, 68, 68],
[46, 53, 65, 68, 68, 68, 68, 68],
[62, 65, 68, 68, 68, 68, 68, 68],
[68, 68, 68, 68, 68, 68, 68, 68]],

[[1, 1, 1, 1, 1, 1, 1, 2],
[1, 1, 1, 1, 1, 1, 1, 2],
[1, 1, 1, 1, 1, 1, 2, 2],
[1, 1, 1, 1, 1, 2, 2, 3],
[1, 1, 1, 1, 2, 2, 3, 3],
[1, 1, 1, 2, 2, 3, 3, 3],
[1, 1, 2, 2, 3, 3, 3, 3],
[2, 2, 2, 3, 3, 3, 3, 3]],

[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 2],
[1, 1, 1, 1, 1, 1, 2, 2],
[1, 1, 1, 1, 1, 2, 2, 3],
[1, 1, 1, 1, 2, 2, 3, 3],
[1, 1, 1, 2, 2, 3, 3, 3],
[1, 1, 2, 2, 3, 3, 3, 3]],


])
            
            photoshopchrom = np.array([
[[29, 41, 52, 34, 20, 20, 17, 17],
[41, 38, 24, 14, 14, 12, 12, 12],
[52, 24, 14, 14, 12, 12, 12, 12],
[34, 14, 14, 12, 12, 12, 12, 12],
[20, 14, 12, 12, 12, 12, 12, 12],
[20, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12]],

[[21, 26, 33, 34, 20, 20, 17, 17],
[26, 29, 24, 14, 14, 12, 12, 12],
[33, 24, 14, 14, 12, 12, 12, 12],
[34, 14, 14, 12, 12, 12, 12, 12],
[20, 14, 12, 12, 12, 12, 12, 12],
[20, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12]],

[[21, 25, 32, 38, 54, 68, 68, 68],
[25, 28, 24, 38, 54, 68, 68, 68],
[32, 24, 32, 43, 66, 68, 68, 68],
[38, 38, 43, 53, 68, 68, 68, 68],
[54, 54, 66, 68, 68, 68, 68, 68],
[68, 68, 68, 68, 68, 68, 68, 68],
[68, 68, 68, 68, 68, 68, 68, 68],
[68, 68, 68, 68, 68, 68, 68, 68]],

[[1, 1, 1, 2, 3, 3, 3, 3],
[1, 1, 1, 2, 3, 3, 3, 3],
[1, 1, 2, 3, 3, 3, 3, 3],
[2, 2, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3]],

[[1, 1,  1, 2, 2, 3, 3, 3],
[1, 1, 1, 2 ,3, 3 ,3 ,3],
[1, 1, 1 ,3 ,3 ,3 ,3, 3],
[2, 2, 3 ,3 ,3 ,3 ,3 ,3],
[2, 3, 3 ,3 ,3 ,3 ,3 ,3],
[3, 3, 3 ,3 ,3 ,3 ,3 ,3],
[3, 3, 3 ,3 ,3 ,3 ,3 ,3],
[3, 3, 3, 3, 3 ,3, 3 ,3]]
            ])
            
            # if qtlum.all() in photoshoplum.all() and qtchrom.all() in photoshopchrom.all():
            #     st.write("photoshop found")
            # else:
            #     st.write("no mathcehes found")
            # lumin = np.array([x[:-1] for x in lumline])

            for i in range(5):
                comparison = photoshoplum[i] == qtlum
                
                comparichrom = photoshopchrom[i] == qtchrom
                
                equal_arrays = comparison.all()
                equal_chrom = comparichrom.all()
                if equal_arrays and equal_chrom:
                    st.error("Found a matching photoshop quantization table")
                        
            
        else:
            st.error("no image selected")
    except AttributeError:
        st.error("no image selected")
    

    