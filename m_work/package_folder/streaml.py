import streamlit as st

import requests
import time

#from PIL import Image ################ ooooooooooooooooooooooo
#from io import BytesIO
#import shutil
import json
from PIL import Image ################ ooooooooooooooooooooooo



st.title("My Smoking Classifier & CTscan Classifier app")
#st.write("Select your features")

tab1, tab2, tab3 = st.tabs(["Tab1: Smoker Status", "Tab2: CTscan Detect Lung Cancer", "Tab3: Important Disclaimer"])
#tab1.write("this is tab 1")
#tab2.write("this is tab 2")

col1, col2 = st.columns([2,1.5])  # 2,1 better!!!!!!!!!!!!
with tab1:
    tab1.markdown("### Input Your Health Biomarkers")
    tab1.markdown("### The ML model will give classification feedback!")
    # Creating four sliders
    #id = st.slider('Select a random value', min_value=10, max_value=100, value=1, step=1)
    #gender = st.selectbox("Gender:", ["F", "M"])
    age = st.slider('Age: Select a value',  min_value=17, max_value=100, value=40, step=1)
    height_cm = st.slider('Height(cm): Select a value',  min_value=50, max_value=230, value=164, step=1)
    weight_kg = st.slider('Weight(Kg): Select a value',  min_value=30, max_value=160, value=65, step=1)
    waist_cm = st.slider('Waist(cm): Select a value',  min_value=40, max_value=140, value=82, step=1)
    eyesight_left = st.number_input(label='eyesight_left (from 0.1 to 9.9)',step=0.1,min_value=0.1,max_value=9.9,value=1., format="%.2f")
    eyesight_right = st.number_input(label='eyesight_right (from 0.1 to 9.9)',step=0.1,min_value=0.1,max_value=9.9,value=1., format="%.2f")
    hearing_left = st.slider('hearing_left: Select a val',  min_value=0.1, max_value=2., value=1., step=1.)
    hearing_right = st.slider('hearing_right: Select a value',  min_value=0.1, max_value=2., value=1., step=1.)
    systolic = st.slider('Systolic: Select a value',  min_value=60, max_value=240, value=120, step=1)
    relaxation = st.slider('Relaxation: Select a value',  min_value=40, max_value=150, value=75, step=1)
    fasting_glucose = st.slider('fasting_glucose: Select a value',  min_value=45, max_value=500, value=100, step=1)
    cholesterol = st.slider('Cholesterol: Select a value',  min_value=55, max_value=450, value=200, step=1)
    triglyceride = st.slider('Triglyceride: Select a value',  min_value=8, max_value=1000, value=125, step=2)
    hdl = st.slider('HDL: Select a value',  min_value=4, max_value=650, value=55, step=3)
    ldl = st.slider('LDL: Select a value',  min_value=1, max_value=1860, value=115, step=1)
    hemoglobin = st.slider('Hemoglobin: Select a value',  min_value=5., max_value=21., value=15., step=1.)
    urine_protein = st.slider('Urine Protein: Select a value',  min_value=1., max_value=6., value=1., step=0.2)
    serum_creatinine = st.slider('Serum Creatinine: Select a value',  min_value=0.1, max_value=11.5, value=0.8, step=0.2)
    ast = st.slider('AST: Select a value',  min_value=6, max_value=1300, value=26, step=2)
    alt = st.slider('ALT: Select a value',  min_value=1, max_value=1500, value=27, step=2)
    gtp = st.slider('GTP: Select a value',  min_value=1, max_value=1000, value=40, step=1)
    #oral = st.selectbox("Oral: Pick one", ["Y", "N"])
    dental_caries = st.slider('Dental Caries: Select a value',  min_value=0., max_value=1., value=0.2, step=0.1)
    tartar = st.selectbox("Tartar: Pick Yes/No", ["Y", "N"])

    #st.slider("Pick a number", 0, 100)
    #st.select_slider("Pick a size", ["S", "M", "L"])
    #st.text_input("First name")
    #st.number_input("Pick a number", 0, 10)
    #st.number_input(label='eyesight_left',step=1,min_value=0.1,max_value=9.9,value=1, format="%.2f")

    # TEST LINE
    #F1={id}&F2h={gender}&F3={age}&F4={height_cm}&F5={weight_kg}&F6={waist_cm}&F7={eyesight_left}&F8={eyesight_right}&F9={hearing_left}&F10={hearing_right}&F11={systolic}&F12={relaxation}&F13={fasting_glucose}&F14={cholesterol}&F15={triglyceride}&F16={hdl}&F17={ldl}&F18={hemoglobin}&F19={urine_protein}&F20={serum_creatinine}&F21={ast}&F22={alt}&F23={gtp}&F24h={oral}&F25={dental_caries}&F26h={tartar}&

    ## UNCOMMENT beloww
    response1 = requests.get(f"https://mvpdraftaaauuu-uzj4hctfqa-ew.a.run.app/predictMLex?F3={age}&F4={height_cm}&F5={weight_kg}&F6={waist_cm}&F7={eyesight_left}&F8={eyesight_right}&F9={hearing_left}&F10={hearing_right}&F11={systolic}&F12={relaxation}&F13={fasting_glucose}&F14={cholesterol}&F15={triglyceride}&F16={hdl}&F17={ldl}&F18={hemoglobin}&F19={urine_protein}&F20={serum_creatinine}&F21={ast}&F22={alt}&F23={gtp}&F25={dental_caries}&F26h={tartar}").json()
    #
    #response1 = requests.get(f"http://127.0.0.1:8000/predictMLex?F3={age}&F4={height_cm}&F5={weight_kg}&F6={waist_cm}&F7={eyesight_left}&F8={eyesight_right}&F9={hearing_left}&F10={hearing_right}&F11={systolic}&F12={relaxation}&F13={fasting_glucose}&F14={cholesterol}&F15={triglyceride}&F16={hdl}&F17={ldl}&F18={hemoglobin}&F19={urine_protein}&F20={serum_creatinine}&F21={ast}&F22={alt}&F23={gtp}&F25={dental_caries}&F26h={tartar}").json()#.text
    #import json
    print(response1)
    #response2 = json.loads(response1)
    st.write("Are you a Smoker?", str(response1['prediction']))


#############################################################################
with tab2:
    tab2.markdown("### Input Your Lung CT scan image")
    tab2.markdown("### VGG16 will tell you in case it finds malignant tissue!")


    col3, col4 = st.columns([1,1])
    with col3:
        uploaded_photo = st.file_uploader("Upload CT scan image")
        #print(uploaded_photo.name)
        camera_photo = st.camera_input("..or take a photo of your scan")
        if camera_photo:
            progress_bar = st.progress(0)
            for perc_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(perc_completed+1)

            tab2.success("CT scan uploaded successfully!")

    with col4:
        #st.write("this is result column")
        if uploaded_photo:
            namingg = st.write("Filename: ", uploaded_photo.name)
            this_photo = uploaded_photo.name
            #print(this_photo+" is HEREEE")

            #'''
            #myio = BytesIO()
            #myio.write(b"Test 123")
            #with open(uploaded_photo.name, "wb") as outfile:
            #    # Copy the BytesIO stream to the output file
            #    outfile.write(myio.getbuffer())
            #'''

            st.write("Please Wait while your Request is Processed")
            time.sleep(5.)
            st.write("Code Running")
            time.sleep(3.)
            st.write("... ... ...")
            time.sleep(2.)

            # problem start##############################################
            # This portion is part of my test code
            #import io

            #byteImgIO = BytesIO()
            #byteImg = Image.open("some/location/to/a/file/in/my/directories.png")
            #byteImg = Image.open("package_folder/" + uploaded_photo.name)

            #byteImg.save(byteImgIO, "PNG")
            #byteImgIO.seek(0)
            #byteImg = byteImgIO.read()

            print("half the test ... ...")
            # Non test code
            #dataBytesIO = BytesIO(byteImg)
            #Image.open(dataBytesIO)

            # problem solved nottt

            displayy = st.image(uploaded_photo)



            #here curl
            headers1 = {
                'accept': 'application/json',
                # requests won't add a boundary if this header is set when you pass files=
                # 'Content-Type': 'multipart/form-data',
            }

            headers2 = {'Content-type': 'application/json', 'Accept': 'text/html'}
            headers3 = {'Content-type': 'multipart/form-data', 'Accept': 'text/html'}
            headers4 = {'Content-type': 'multipart/form-data', 'Accept': 'text/plain'}
            headers5 = {'Accept': 'text/html'}

            #cached_pic_link = uploaded_photo.name
            #st.write(cached_pic_link)
            if uploaded_photo is not None:
                # Display uploaded image
                image = Image.open(uploaded_photo)
                uploaded_photo.seek(0)
                files = {'file': uploaded_photo}
                uploaded_photo.seek(0)

                response = requests.post('https://mvpdraftaaauuu-uzj4hctfqa-ew.a.run.app/uploadfile',files=files).json()#headers
                #response = requests.post('http://127.0.0.1:8000/uploadfile',files=files).json()#headers

                #print(response.status_code)
                #print(response.text)
                st.write("Cancer Detection response?", str(response['prediction']))

            #h = requests.head('https://mvpdraftaaalll-uzj4hctfqa-ew.a.run.app/uploadfile/', headers=headers,files=files)
            #header = h.headers
            #contentType = header.get('content-type')
            #print(contentType)  ######################### text/html; charset=UTF-8
            print("THERE u go below!!!!!!!!!!!!!!")

            print("THERE u go above!!!!!!!!!!!!!!")

            #r2d2 = requests.post('https://mvpdraftaaalll-uzj4hctfqa-ew.a.run.app/uploadfile/',files=files).text#headers
            #print(r2d2)
            #print("r2d2 printed above no?")
            #import json
            #r2d3 = json.loads(r2d2)
            #print(r2d3)
            #print("test overrr")


            #from pprint import pprint
            #pprint(requests.post('https://mvpdraftaaalll-uzj4hctfqa-ew.a.run.app/uploadfile/', files=files).json()['headers'])
            #print("test overrr")




        if camera_photo:
            st.write("model running on ur CTscan noww- out of service")


with tab3:
    tab3.markdown("## Important Disclaimer")
    tab3.markdown("### This Project was implemented as part of an educational exercise. No interaction with our api nor streamlit front-end can be interpreted as medical advice.")





#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')
