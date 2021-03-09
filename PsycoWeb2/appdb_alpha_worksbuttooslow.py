
import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np


import pymongo
client = pymongo.MongoClient("mongodb+srv://psycov1:8JchK914zXFv00YM@cluster0.eaq0i.mongodb.net/Psycov05?retryWrites=true&w=majority")
db = client.Psycov05
collection = db.Psycov05collection




st.write("""Exploration of PsyCOVID database""")

progress_bar = st.sidebar.progress(1)
status_text = st.sidebar.empty()    

data = pd.read_csv('cleaned.csv', error_bad_lines=False, encoding='latin-1').fillna(0)

kwargs = {}

b_age = st.sidebar.checkbox('Age', value=True)
if b_age:
    kwargs['Dem_age'] = str(st.sidebar.slider("Choose age:", 18, 70))

b_gender = st.sidebar.checkbox('Gender', value=True)
if b_gender: 
    kw_gender = {}
    kw_gender['$in']= st.sidebar.multiselect('Pick a gender',  options=['Male','Other/would rather not say','Female'], default='Female')
    kwargs['Dem_gender']= kw_gender


b_country = st.sidebar.checkbox('Country', value=False)
if b_country:
    kw_country = {}
    kw_country['$in']= st.sidebar.multiselect("Pick a country", collection.distinct( "Country" ))
    kwargs['Country']= kw_country


w_attribute_labels = ['neu','ext','ope','agr','con']

st.write(kwargs)

def reckon_attr(document, filter = w_attribute_labels):
    return [float(document[x]) for x in filter]

    
def datamix(kwargs): 
    cursor = collection.find(kwargs)
    df_f = pd.DataFrame(columns =  w_attribute_labels)
    for document in cursor: 
        df_f.loc[len(df_f)] = (reckon_attr(document))
    return df_f
    

def make_radar_chart(name="Big 5"):
    if datamix(kwargs).empty:
        return st.write('Insufficient data. Please modify your query.')
    markers = list(datamix(kwargs).mean()) 


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
    ax.set_title(name+': The pentagonal chart you see applies for '+str(len(datamix(kwargs)))+' people')
    ax.grid(True)



    return st.pyplot(fig)

make_radar_chart()
#datamix()
