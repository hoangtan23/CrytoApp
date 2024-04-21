

import pandas as pd
import plotly.express as px
#import streamlit as st
import altair as alt

df = pd.read_csv('edit.csv')


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
 st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard Cryto')

query = st.sidebar.text_input("Search Coin")


st.sidebar.markdown('''
---
Created with ❤️ by Tran Hoang Tan.
''')


col1, col2 = st.columns((6,4))

with col1:
 st.markdown('Market Cap Top 200 Coin')
 #fig = px.treemap(df, path=[px.Constant("Market_cap"), 'Coin'], values='Market_cap',color_continuous_scale='RdBu')

 #st.plotly_chart(fig, theme="streamlit")


with col2:
    tab1, tab2 = st.tabs(["Top 5 Coin Up 24H", "Top 5 Coin Down 24H"])

    with tab1:
        dfUP= df.sort_values(by='Price_change_24h',ascending=False).iloc[:,:4].head(5)
        st.data_editor(
        dfUP,
        hide_index=True
        )    

    with tab2:
        dfDOWN= df.sort_values(by='Price_change_24h',ascending=True).iloc[:,:4].head(5)
        st.data_editor(
        dfDOWN,
        hide_index=True, 
        ) 
    
st.markdown('Percentage price change 1day/90days')
chart = alt.Chart(df).mark_circle().encode(
    x='Price_change_24h',
    y='Price_change_90d',
    color='Coin',
    ).interactive()

st.altair_chart(chart, theme=None, use_container_width=True)

    
st.markdown('Top 200 Coin')

if query:
    mask = df.applymap(lambda x: query in str(x).lower()).any(axis=1)
    df = df[mask]

st.data_editor(
    df,
    hide_index=True, 
) 
