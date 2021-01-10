import streamlit as st
from PIL import Image 


st.write(""" # Image Compressor """)
st.write(""" ## Made by: Shivam Bhosale """)
uploaded_file = st.file_uploader("Upload your Image to be compressed here, As of now it only accepts jpg images and reduces their dimension thereby compressing the image", type=".jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image',width=300)
    st.write("The image is compressed")
    
    if st.button('Download'):
        st.write("To Download the Image right-click on the image and select 'Save Image As' ")