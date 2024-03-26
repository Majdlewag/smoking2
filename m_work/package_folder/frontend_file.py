import streamlit as st
import requests
import time

st.title("My iris classifier app")

st.write("Select your features")

col1, col2 = st.columns([2,1])

col1.markdown("## Input Your Health Biomarkers")
col1.markdown("## The ML model will give classification feedback!")
# Creating four sliders
value1 = st.slider('Select a value', min_value=0, max_value=4, value=1, step=1)
value2 = st.slider('Select a value',  min_value=0, max_value=4, value=1, step=1)
value3 = st.slider('Select a value',  min_value=0, max_value=4, value=1, step=1)
value4 = st.slider('Select a value',  min_value=0, max_value=4, value=1, step=1)

# TEST LINE
response = requests.get(f"https://mvp-b3jhtp774a-ew.a.run.app/predict?sepal_length={value1}&sepal_width={value2}&petal_length={value3}&petal_width={value4}").json()
st.write("The flower belongs to class", str(response['prediction']))


#############################################################################
col2.markdown("## Input Your Lung CT scan image")
col2.markdown("## VGG16 will tell you in case it finds malignant tissue!")

uploaded_photo = col2.file_uploader("Upload CT scan image")
camera_photo = col2.camera_input("..or take a photo of your scan")
progress_bar = col2.progress(0)
for perc_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)

col2.success("CT scan uploaded successfully!")
