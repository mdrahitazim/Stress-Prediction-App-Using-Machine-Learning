import streamlit as st
import pandas as pd
import numpy as np
import pickle
#import cv2
#import PIL.Image

#if not hasattr(PIL.Image,'Resampling'):
#    PIL.Image.Resampling = PIL.Image
#AttributeError: module 'PIL.Image' has no attribute 'Resampling'


#description of webapp
st.title("Are you stressed ?")

#adding header image
#image = cv2.imread("image.jpeg")
#st.image(image, channels="BGR",output_format="JPEG")

st.title("Determine whether you are stressed or not from the lifestyle you are leading")
st.write("Here is a way to check your level of stress from the lifestyle you are living")
st.write("Based on your choice, you will fall under this categories")
st.write('''
    1. No stress in your life :thumbsup:
    
    2. Severe stress

    3. Minor stress
    
    4. Bearable stress
    
    5. High stress''')

st.divider()

st.title("Check your stress")
#inputs 
st.write("~ keep the slider to 0, if you don't spend time on some activies listed below")
st.write("In a DAY -")
Mobile = st.slider(
    'How much do you use your mobile phone? (answer in term of hours)',
     0, 24)
st.write('Mobile Usage Time:', Mobile,'hours')

Laptop = st.slider(
    'How much do you use your Laptop phone? (answer in term of hours)',
     0, 25)
st.write('Laptop Usage Time:', Laptop,'hours')


Gaming = st.slider(
    'Do you play video games (in hours)',
     0, 23)
st.write('Gaming time:',Gaming, 'hours')


TV = st.slider(
    'How much TV are you watching (in hours)',
     0, 22)
st.write('TV time:',TV,'hours')


Music = st.slider(
    'How much music do you listen (in hours)',
     0, 21)
st.write('Music:',Music,'hours')


Work = st.slider(
    'For working professionals - How many hours do you work (in hours)',
     0, 20)
st.write('Hours spent on working:',Work)


Study = st.slider(
    'For students - How many hours do you study (in hours)',
     0, 19)
st.write('Study hours:',Study)


OutdoorGameExercise = st.slider(
    'Outdoor Games or exercise ime (in hours)',
     0, 18)
st.write('Values:', OutdoorGameExercise)



Socialization = st.slider(
    'Socialization Time (in hours)',
     0, 17)
st.write('Socialization:',Socialization)


FreeMind = st.slider(
    'How much time you give yourself free, time when you reciprocate (in hours)',
     0, 3)
st.write('Free Mind:',FreeMind, 'hours')


Sleep = st.slider(
    'How many hours do you sleep',
     0, 15)
st.write('Sleep:',Sleep, 'hours')


Meditation = st.slider(
    'Do you meditate (in hours)',
     0.0, 2.0)
st.write('Meditation:', Meditation, 'hours')




#process


columns = ['Mobile', 'Laptop', 'Gaming', 'TV', 'Music', 'Work', 'Study',
       'Outdoor Game/Exercise', 'Socialization', 'Free Mind', 'Sleep',
       'Meditation']
filename = "stress_prediction_model.pkl"


with open(filename,'rb') as file:
    model = pickle.load(file)


def predict():
    row = np.array([Mobile, Laptop, Gaming, TV, Music, Work, Study,OutdoorGameExercise, Socialization, FreeMind, Sleep, Meditation])
    X = pd.DataFrame([row], columns= columns)
    pred = model.predict(X)

    print(pred)
    st.title("Result")
    if pred <= 0:
        pred = 1
        st.success("No stress in your life :thumbsup:")
    elif pred > 75:
        st.success("Severe stress")
        if pred >100:
            pred = 100
    elif pred > 0 and pred <= 20:
        st.success("Minor Stress")
    elif pred > 20 and pred <= 50:
        st.success("Bearable Stress")
    elif pred > 50 and pred <= 75:
        st.success("High Stress")
    
    #graph at result
    stress = int(pred)
    st.title("Stress Bar")
    st.write("stress level: ",stress, "%")
    st.progress(stress/100)
    st.write("low = 0% and high = 100%")
    st.divider()

if st.button("Predict"):
    predict()
