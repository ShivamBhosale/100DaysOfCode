import streamlit as st
import tensorflow as tf
import requests
st.set_option('deprecation.showfileUploaderEncoding',False)
@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model('PDDV1.hdf5')
    return model
model=load_model()
st.write(""" # Plant Disease Detection """ )
st.write(""" ### Prototype - 2 """)
file= st.file_uploader("Upload a leaf image to make a prediction",type=['jpg',"png"])

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
    st.text("Please Upload a leaf image file of size (256X256)")
else:
    image = Image.open(file)
    st.image(image,width=300)
    predictions = import_and_predict(image,model)
    class_names = ["Pepper bacterial spot","Pepper healthy","Tomato early blight","Tomato healthy","Tomato Spider mites"]
    string="The above leaf is most likely to be: "+class_names[np.argmax(predictions)]
    st.success(string) 
    st.text("You are a bad boy")


