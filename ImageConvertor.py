
import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

def img_grayscale(image_convert):
    img = Image.open(image_convert)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)


with st.expander("Start camera"):
     camera_image = st.camera_input("Camera")

if camera_image:
     img_grayscale(camera_image)


