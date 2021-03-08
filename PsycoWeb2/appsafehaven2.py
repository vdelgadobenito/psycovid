
import streamlit as st
import time
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import requests






st.write("""My first app COpsych""")

progress_bar = st.sidebar.progress(1)
status_text = st.sidebar.empty()    

data = pd.read_csv('covfinal.csv', error_bad_lines=False, encoding='latin-1').fillna(0)

b_age = st.sidebar.checkbox('Age')

if b_age:
    w_age = st.slider("Choose age:", 18, 70)

w_gender = st.sidebar.select_slider('Pick a gender',  options=['Male','Other/would rather not say','Female'], value='Other/would rather not say')
#w_language = st.radio("Pick a language", ('EN','FR','PL','DE','PT'))
w_country = st.sidebar.multiselect("Pick a country", data['Country'].unique())


if w_gender == 'Female':
    st.write('You selected female')
elif w_gender == 'Male':
    st.write('You selected male')
else: 
    st.write('You selected other genders')


w_attribute_labels = ['neu','ext','ope','agr','con']


def datagender(gender='Female'):
    return data.loc[data['Dem_gender']==gender]

def datacountry(country='Poland'):
    return data.loc[data['Country']==country]
    

def datalanguage(UserLanguage='PL'):
    return data.loc[data['UserLanguage']==UserLanguage]
    
def datamix(gender= w_gender, country=w_country): #UserLanguage=w_language, has been removed for now
    if b_age: 
        mix = data.loc[data['Dem_gender']==gender].loc[data['Country']==country].loc[data['Dem_age']==w_age] #.loc[data['UserLanguage']==UserLanguage] has been removed for now
    else:
        mix = data.loc[data['Dem_gender']==gender].loc[data['Country'].isin(country)]
    if len(mix)>0:
        return mix[w_attribute_labels],len(mix)
    else:
        return 'err1' #This is only a placeholder for insufficient data


def make_radar_chart(name="Big 5"):
    if datamix() == 'err1':
        return st.write('Insufficient data')
    markers = list(datamix()[0].mean()) 


    labels = np.array(w_attribute_labels)
    
    plot_markers = markers
    stats= markers    
        
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    
#     stats = np.concatenate((stats))
#     angles = np.concatenate((angles))

    fig= plt.figure(figsize=(10, 15), dpi=80, facecolor='w', edgecolor='red')
    ax = fig.add_subplot(111, polar=True)
#     ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.yticks(markers)
    ax.set_title(name)
    ax.grid(True)



    return st.pyplot(fig)

make_radar_chart()