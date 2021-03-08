
import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np







st.write("""Exploration of PsyCOVID database""")

progress_bar = st.sidebar.progress(1)
status_text = st.sidebar.empty()    

data = pd.read_csv('covfinal.csv', error_bad_lines=False, encoding='latin-1').fillna(0)

kwargs = {}

b_age = st.sidebar.checkbox('Age', value=True)
if b_age:
    kwargs['Dem_age'] = st.sidebar.slider("Choose age:", 18, 70)

b_gender = st.sidebar.checkbox('Gender', value=True)
if b_gender: 
    kwargs['Dem_gender'] = st.sidebar.multiselect('Pick a gender',  options=['Male','Other/would rather not say','Female'], default='Female')

b_country = st.sidebar.checkbox('Country', value=False)
if b_country:
    kwargs['Country'] = st.sidebar.multiselect("Pick a country", data['Country'].unique())

b_language = st.sidebar.checkbox('Language of the survey', value=False)
if b_language:
    kwargs['UserLanguage'] = st.sidebar.multiselect("Pick a language", data['UserLanguage'].unique())

b_comment = st.sidebar.checkbox('I want to add a comment', value=False)
if b_comment:
    txt = st.text_area('Your feelings', '''The user will be able to put some comment here which will go through NLP''')
#st.write('Sentiment:', run_sentiment_analysis(txt))    


w_attribute_labels = ['neu','ext','ope','agr','con']

st.write(kwargs)

    
def datamix(**kwargs): #UserLanguage=w_language, has been removed for now
    mix = data
    for key, value in kwargs.items():
        
        if type(value) is list:
            mix = mix.loc[data[key].isin(value)] #cast a list or a string
            
        else: 
            mix = mix.loc[data[key]==value]

    #st.write('mix cast:',locals()['mix'])



    return mix[w_attribute_labels]
 


def make_radar_chart(name="Big 5"):
    if datamix(**kwargs).empty:
        return st.write('Insufficient data. Please modify your query.')
    markers = list(datamix(**kwargs).mean()) 


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
    ax.set_title(name+': The pentagonal chart you see applies for '+str(len(datamix(**kwargs)))+' people')
    ax.grid(True)



    return st.pyplot(fig)

make_radar_chart()
#datamix()