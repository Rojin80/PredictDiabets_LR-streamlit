import streamlit as st
import pickle 

pickle_in = open("lr.pkl" , 'rb')
classifier = pickle.load(pickle_in)

st.header("Diabets Prediction")
st.sidebar.header("diabets prediction")

if not st.sidebar.checkbox("hide" , True , key="2"):
    st.title("Diabets Prediction(only for female above 21 years old;)")
    name = st.text_input("Name:")
    pregency = st.number_input("Pregnancies:")
    glucose = st.number_input("Glucose:")
    bp = st.number_input("BloodPressure:")
    skin = st.number_input("SkinThickness:")
    insulin = st.number_input("Insulin:")
    bmi = st.number_input("BMI:")
    dpf = st.number_input("DiabetesPedigreeFunction:")
    age = st.number_input("Age:")
    
    submit = st.button("Predict")
    
    if submit:
        prediction = classifier.predict([[pregency , glucose , bp , skin , insulin , bmi , dpf , age]])
        if prediction == 0 :
            st.write("Congratulations!" , name , "You are not diabetic")
        else :
            st.write(name , "we are really sorry to say but like you are Diabetic, but don't lose your hope")
