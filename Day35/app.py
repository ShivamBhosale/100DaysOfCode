import streamlit as st
import tensorflow as tf

st.set_option('deprecation.showfileUploaderEncoding',False)
@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model('rps.h5')
    return model
model=load_model()
st.write(""" # Rock Paper Scissor Hand Gesture Recognizer """ )

file= st.file_uploader("Upload an Image to make a prediction",type=['jpg',"png"])

import cv2 
from PIL import Image, ImageOps
import numpy as np
 
def import_and_predict(image_data,model):
    size = (300,300)
    img = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape= img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please Upload an image file")
else:
    image = Image.open(file)
    st.image(image,width=300)
    predictions = import_and_predict(image,model)
    class_names = ["Paper","Rock","Scissor"]
    string="The above gesture is most likely to be: "+class_names[np.argmax(predictions)]
    st.success(string)
