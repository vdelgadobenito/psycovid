
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

data = pd.read_csv('covfinal.csv', error_bad_lines=False, encoding='latin-1')

kwargs = {}

b_age = st.sidebar.checkbox('Age', value=True)
if b_age:
    kwargs['Dem_age'] = st.slider("Choose age:", 18, 70)

b_gender = st.sidebar.checkbox('Gender', value=True)
if b_gender: 
    kwargs['Dem_gender'] = st.sidebar.multiselect('Pick a gender',  options=['Male','Other/would rather not say','Female'])
#w_language = st.radio("Pick a language", ('EN','FR','PL','DE','PT'))
b_country = st.sidebar.checkbox('Country', value=True)
if b_country:
    kwargs['Country'] = st.sidebar.multiselect("Pick a country", ('France','Germany','Poland','Denmark','Spain'))

def greet_me(**kwargs):
    for key, value in kwargs.items():
        st.write("{0} = {1}".format(key, value))
        #if type(value) is list:
        #   mix = .loc[data['{0}'.format(key)].isin(value) #cast a list or a string
        #else: 
        #   mix = loc[data['{0}'.format(key)]='{0}'.format(value)

greet_me(**kwargs)



w_attribute_labels = ['neu','ext','ope','agr','con']


def datagender(gender='Female'):
    return data.loc[data['Dem_gender']==gender]

def datacountry(country='Poland'):
    return data.loc[data['Country']==country]
    

def datalanguage(UserLanguage='PL'):
    return data.loc[data['UserLanguage']==UserLanguage]
    
def datamix(**kwargs): #UserLanguage=w_language, has been removed for now

# try casting kwargs directly to mix variable
    mix = data
    for key, value in kwargs.items():
        
        if type(value) is list:
            mix = mix.loc[data[key].isin(value)] #cast a list or a string
            pass
        else: 
            mix = mix.loc[data[key]==value]



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