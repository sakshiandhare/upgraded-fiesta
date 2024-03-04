import streamlit as st
import requests

API_URL = 'https://dental-app1.onrender.com/predict'

def predict_image(image):
    try:
        files = {'file': image}
        response = requests.post(API_URL, files=files)
        if response.status_code == 200:
            return response.json()['predicted_class']
        else:
            return "Error: " + response.text
    except Exception as e:
        return "An error occurred: " + str(e)

def main():
    st.title("Dental Image Classifier")
    uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        if st.button("Predict"):
            predicted_class = predict_image(uploaded_image)
            st.write("Predicted Class:", predicted_class)

if __name__ == '__main__':
    main()
