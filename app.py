import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')

df=pd.read_csv('india.csv')
df=df.drop(columns=['Literate'])
a=list(df['State'].unique())
a.insert(0,'OverAll India')
b=sorted(df.columns[6:])
st.title('Understand India Better')
# st.text('Please Select the Viz from Sidebar')
st.sidebar.title('Understand India Better')
State_name=st.sidebar.selectbox('Select State name',a)
First =st.sidebar.selectbox('Select Primary Parameter',b)
Second =st.sidebar.selectbox('Select Secondary Parameter',b)
button=st.sidebar.button('Get')
if button:
    if State_name=='OverAll India':
        st.title(State_name)
        st.text('*Size represents Frist parameter')
        st.text('*Colour represents Second parameter')
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=First,color=Second,mapbox_style='carto-positron',color_continuous_scale="Hot",zoom=4,height=700,width=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        new_df=df[df['State']==State_name]
        st.title(State_name)
        st.text('*Size represents Frist parameter')
        st.text('*Colour represents Second parameter')
        fig=px.scatter_mapbox(new_df,lat='Latitude',lon='Longitude',size=First,color=Second,mapbox_style='carto-positron',color_continuous_scale="Hot",zoom=5,height=700,width=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
