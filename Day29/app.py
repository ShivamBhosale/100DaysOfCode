import streamlit as st
import tensorflow as tf

st.set_option('deprecation.showfileUploaderEncoding',False)
@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model('plant5.hdf5')
    return model
model=load_model()
st.write(""" # Plant Disease Detection """ )
st.write(""" ### Made by Shivam Bhosale and Shubham Pandey """)
file= st.file_uploader("Upload an Image to make a prediction",type=['jpg',"png"])

import cv2 
from PIL import Image, ImageOps
import numpy as np
 
def import_and_predict(image_data,model):
    size = (256,256)
    img = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape= img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please Upload a leaf image file")
else:
    image = Image.open(file)
    st.image(image,width=300)
    predictions = import_and_predict(image,model)
    class_names = ["Pepper bacterial spot","Pepper healthy","Tomato early blight","Tomato healthy"]
    string="The above leaf is most likely to be: "+class_names[np.argmax(predictions)]
    st.success(string) 
    st.write(np.argmax(predictions))
