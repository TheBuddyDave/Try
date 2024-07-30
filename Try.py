

import streamlit as st


st.header('The Math')
with st.expander("CLICK TO SHOW AND HIDE THE MATH (its kinda long)"):

    image_files = ['abc.jpg'] 


#show the math images(couldnt get the pdf to work and wasnt worth the effort)
    for img in image_files:
            st.image(img)

