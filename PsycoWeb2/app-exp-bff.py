
import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np



bff15_options = {
    'Strongly disagree':1,'Disagree':2,'Slightly disagree':3,'Slightly agree':4,'Agree':5,'Strongly agree':6
}



st.write("""Exploration of PsyCOVID database""")

progress_bar = st.sidebar.progress(1)
status_text = st.sidebar.empty()    

data = pd.read_csv('covfinal.csv', error_bad_lines=False, encoding='latin-1').fillna(0)

kwargs = {}

st.sidebar.write("""I see myself as a person who...""")


kwargs['BFF_15_1']  = st.sidebar.select_slider('... is often concerned', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_1')[1]
#st.sidebar.write('My favorite color is', kwargs['BFF_15_1'])
kwargs['BFF_15_2']  = st.sidebar.select_slider('... easily gets nervous ', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_2')[1]
kwargs['BFF_15_3']  = st.sidebar.select_slider('... is good at staying cool in stressful situations ', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_3')[1]
kwargs['BFF_15_4']  = st.sidebar.select_slider('... likes to chat', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_4')[1]
kwargs['BFF_15_5']  = st.sidebar.select_slider('... is extrovert and sociable', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_5')[1]
kwargs['BFF_15_6']  = st.sidebar.select_slider('... is socially reserved', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_6')[1]
kwargs['BFF_15_7']  = st.sidebar.select_slider('... gets a lot of new ideas', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_7')[1]
kwargs['BFF_15_8']  = st.sidebar.select_slider('... appreciates arts and aesthetics', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_8')[1]
kwargs['BFF_15_9']  = st.sidebar.select_slider('... has a vivid imagination and can think of things that do not yet exist ', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_9')[1]
kwargs['BFF_15_10']  = st.sidebar.select_slider('... is sometimes impolite to others', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_10')[1]
kwargs['BFF_15_11']  = st.sidebar.select_slider('... is forgiving towards others', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_11')[1]
kwargs['BFF_15_12']  = st.sidebar.select_slider('... is kind and condierate towards almost everyone', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_12')[1]
kwargs['BFF_15_13']  = st.sidebar.select_slider('... is thorough and meticulous', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_13')[1]
kwargs['BFF_15_14']  = st.sidebar.select_slider('... is lazy', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_14')[1]
kwargs['BFF_15_15']  = st.sidebar.select_slider('... is effective when I do something', list(bff15_options  .items()), format_func=lambda o: o[0], key='BFF_15_15')[1]




w_attribute_labels = ['neu','ext','ope','agr','con']



    
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