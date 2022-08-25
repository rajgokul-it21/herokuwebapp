# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:07:11 2022

@author: student
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(
        page_title="Disease Predictor",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )




diabetes_model = pickle.load(open('C:\machine learning/diabetes_model.sav', 'rb'))

Autism_model = pickle.load(open('C:\machine learning\Autism_model.sav','rb'))

parkinsons_model = pickle.load(open('C:\machine learning/parkinsons_model (1).sav', 'rb'))




    
selected = option_menu('Real Time Disease Prediction System',
                           
                          
                          ['Home','Diabetes Prediction',
                           'Autism Prediction',
                           'Parkinsons Prediction','Precautions'],
                          
                          icons=['house-fill','activity','heart','person','shield-fill-plus'], menu_icon="cast",
                          default_index=0,orientation="horizontal")
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('CHECK UP'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Autism Disease Prediction Page
if (selected == 'Autism Prediction'):
    
    # page title
    st.title('Autism Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        A1_Score = st.text_input('A1_Score')
        
    with col2:
        A2_Score = st.text_input('A2_Score')
        
    with col3:
        A3_Score = st.text_input('A3_Score')
        
    with col1:
        A4_Score = st.text_input('A4_Score')
        
    with col2:
        A5_Score = st.text_input('A5_Score')
        
    with col3:
        A6_Score = st.text_input('A6_Score')
        
    with col1:
        A7_Score = st.text_input('A7_Score')
        
    with col2:
        A8_Score = st.text_input('A8_Score')
        
    with col3:
        A9_Score = st.text_input('A9_Score')
        
    with col1:
        A10_Score = st.text_input('A10_Score')
        
    with col2:
        age = st.text_input('age')
        
    with col3:
            gender = st.text_input('gender')
            
    with col1:
           jaundice = st.text_input('jaundice')
         
    with col2:
        autism = st.text_input('autism')
        
    with col3:
        result = st.text_input('result')
        

        
        
     
     
    # code for Prediction
    autism_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button("CHECK UP"):
        autism_prediction = Autism_model.predict([[A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score,A8_Score,A9_Score,A10_Score,age,gender,jaundice,autism,result]])                          
        
        if (autism_prediction[0] == 1):
         autism_diagnosis = 'The person is having autism disease'
        else:
          autism_diagnosis = 'The person does not have any autism disease'
        
    st.success(autism_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction ")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("CHECK UP"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
#precaustion
if (selected == 'Precautions'):
    
    
    st.title('Measures to maintain health')
    
    
    col1, col2, col3 = st.columns(3)

    with col1:
     st.header("Diabetes")
     st.write('''
    1.Make a commitment to managing your diabetes\n
    2. Don't smoke\n
    3. Keep your blood pressure and cholesterol under control\n
    4. Schedule regular physicals and eye exams\n
    5. Keep your vaccines up to date\n
    6. Take care of your teeth\n
    7. Pay attention to your feet\n
    8. Consider a daily aspirin\n
    9.. If you drink alcohol, do so responsibly\n
    10. Take stress seriously
    ''')

    with col2:
     st.header("Autism")
     st.write('''
     1.Behavioral management therapy\n
     2.Cognitive behavior therapy\n
     3.Early intervention\n
     4.Educational and school-based therapies\n
     5.Joint attention therapy\n
     6.Medication treatment\n
     7.Nutritional therapy\n
     8.Occupational therapy\n
     9.Parent-mediated therapy\n
     10.Physical therapy\n
     11.Social skills training\n
    12.Speech-language therapy\n
    ''')
   

    with col3:
     st.header("Parkinson's")
     st.write('''
    1.Go Organic (and Local)\n
    2.Eat Fresh, Raw Vegetables\n
    3.Incorporate Omega-3 Fatty Acids Into Your Diet\n
    4.Vitamin D3\n
    5.Green Tea\n
    6.Regular Aerobic Exercise\n
    7.CoQ10\n
    ''')
    
    
  
    
    



