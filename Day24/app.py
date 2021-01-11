import streamlit as st
import tensorflow as tf

st.set_option('deprecation.showfileUploaderEncoding',False)
@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model('Cat_Dog.hdf5')
    return model
model=load_model()
st.write(""" # Cat and Dog Classifier """ )
file= st.file_uploader("Upload an Image to make a prediction",type=['jpg',"png"])

import cv2 
from PIL import Image, ImageOps
import numpy as np
 
def import_and_predict(image_data,model):
    size = (150,150)
    img = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape= img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please Upload a image file")
else:
    image = Image.open(file)
    st.image(image,width=300)
    predictions = import_and_predict(image,model)
    if predictions[0]>0:
        string="The uploaded image is of a Dog."
    else:
        string="The uploaded image is of a Cat."
    st.success(string)



