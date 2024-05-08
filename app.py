import streamlit as st
import cv2
from PIL import Image
import numpy as np

def cartoonify_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply median blur to smoothen the image
    gray = cv2.medianBlur(gray, 5)
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to reduce color palette and smooth out colors
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

def main():
    st.title("Image Cartoonifier")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Original Image', use_column_width=True)

        # Convert image to numpy array
        img_array = np.array(image)

        # Cartoonify the image
        cartoon_image = cartoonify_image(img_array)

        # Convert numpy array back to image
        cartoon_img_pil = Image.fromarray(cartoon_image)

        st.image(cartoon_img_pil, caption='Cartoonified Image', use_column_width=True)

if __name__ == "__main__":
    main()
